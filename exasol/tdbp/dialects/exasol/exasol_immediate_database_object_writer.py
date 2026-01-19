from typing import override

from pyexasol import ExaConnection

from exasol.tdbp.database_object import DatabaseObject
from exasol.tdbp.database_object_listener import DatabaseObjectListener
from exasol.tdbp.schema import Schema
from exasol.tdbp.table import Table


class ExasolImmediateDatabaseObjectWriter(DatabaseObjectListener):
    """Listens to database object events and writes the object to Exasol immediately."""

    def __init__(self, connection: ExaConnection):
        """
        Initializes the class with a provided database connection instance.

        Args:
            connection (ExaConnection): A connection to the Exasol database.
        """
        self.connection = connection

    @override
    def on_create(self, database_object: DatabaseObject) -> None:
        """A database object was created.

        Args:
            database_object (DatabaseObject): The database object that was created.
        """
        sql = ""
        if isinstance(database_object, Schema):
            sql = f"""CREATE SCHEMA {database_object.fully_qualified_name()};"""
        elif isinstance(database_object, Table):
            print(f"Columns: {database_object.columns}")
            column_definitions = [
                f""""{key}" {value}""" for key, value in database_object.columns.items()
            ]
            sql = f"""CREATE TABLE {database_object.fully_qualified_name()}({", ".join(column_definitions)})"""
        self.connection.execute(sql)
        self.connection.commit()

    @override
    def on_insert(self, table: Table, values: list) -> None:
        """
        A row was inserted into a table.

        Args:
            table (Table): The table where the row was inserted.
            values (list): The values of the inserted row.
        """
        self.on_insert_all(table, [values])

    @override
    def on_insert_all(self, table: Table, values: list[list]) -> None:
        """
        Rows were inserted into a table.

        Args:
             table (Table): The table where the rows were inserted.
             values (list[list]): A list of lists, where each inner list represents a row.
        """
        self.connection.ext.insert_multi(
            (table.schema.identifier, table.identifier), values
        )
        self.connection.commit()

    @override
    def purge_user_objects(self) -> None:
        """Removes all user objects from the database.

        A user object is any database object created by the user in contrast
        to system objects, which are created by the database itself.

        The purpose of this method is to ensure a clean database for testing.

        System objects in Exasol are, for example, all tables and views in the SYS schema.
        Those are not touched by this method.
        """
        with self.connection.execute(
            "SELECT schema_name FROM sys.exa_dba_schemas"
        ) as statement:
            for row in statement:
                self.connection.execute(f"DROP SCHEMA {row[0]} CASCADE")
            self.connection.commit()
