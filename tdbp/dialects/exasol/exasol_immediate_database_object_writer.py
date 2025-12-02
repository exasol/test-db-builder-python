from tdbp.DatabaseObjectWriter import DatabaseObjectWriter
from tdbp.schema import Schema
from tdbp.dialects.exasol.exasol_connection_factory import connect


class ExasolImmediateDatabaseObjectWriter(DatabaseObjectWriter):
    def write(self, schema: Schema) -> None:
        with connect() as connection:
            connection.execute(f"CREATE SCHEMA {schema.name}")
            connection.commit()



    def purge_user_objects(self):
        with connect() as connection:
            with connection.execute("SELECT SCHEMA_NAME FROM SYS.EXA_DBA_SCHEMAS") as statement:
                for row in statement:
                    connection.execute(f"DROP SCHEMA {row[0]} CASCADE")
                connection.commit()
