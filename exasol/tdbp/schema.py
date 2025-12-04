from typing import override

from exasol.tdbp.database_object import DatabaseObject
from exasol.tdbp.database_object_listener import DatabaseObjectListener
from exasol.tdbp.table import Table


class Schema(DatabaseObject):
    """
    Represents a database schema.

    Attributes:
        name (str): The name of the schema as defined when creating the instance.
        listener (DatabaseObjectListener): Listener object that handles database
            object events.
    """

    def __init__(self, listener: DatabaseObjectListener, schema_name: str):
        super().__init__(listener, schema_name)

    @override
    def fully_qualified_name(self) -> str:
        return f'"{self.name}"'

    def create_table(self, table_name: str, **columns):
        """
        Creates a new table with the specified name and columns.

        Args:
            table_name (str): The name of the table to be created.
            **columns: Arbitrary keyword arguments representing the columns and their
                definitions for the table.

        Returns:
            Table: The newly created Table object.
        """
        table = Table(self.listener, table_name, self, **columns)
        self.listener.on_create(table)
        return table
