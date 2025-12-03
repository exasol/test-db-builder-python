from tdbp.database_object import DatabaseObject
from tdbp.database_object_listener import DatabaseObjectListener
from tdbp.table import Table
from tdbp.schema import Schema
from tdbp.dialects.exasol.exasol_connection_factory import connect


class ExasolImmediateDatabaseObjectListener(DatabaseObjectListener):
    def on_create(self, database_object: DatabaseObject) -> None:
        sql = ""
        if isinstance(database_object, Schema):
            sql = f"""CREATE SCHEMA "{database_object.name}";"""
        elif isinstance(database_object, Table):
            column_definitions = [f""""{key}" {value}""" for key, value in database_object.columns]
            sql = f"""CREATE TABLE "{database_object.name}"({", ".join(column_definitions)})"""
        with connect() as connection:
            print("SQL: " + sql)
            connection.execute(sql)
            connection.commit()




    def purge_user_objects(self):
        with connect() as connection:
            with connection.execute("SELECT SCHEMA_NAME FROM SYS.EXA_DBA_SCHEMAS") as statement:
                for row in statement:
                    connection.execute(f"DROP SCHEMA {row[0]} CASCADE")
                connection.commit()
