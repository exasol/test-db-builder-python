from tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory
from tdbp.dialects.exasol.exasol_connection_factory import connect


def test_purge_user_objects() -> None:
    with connect() as connection:
        connection.execute("CREATE SCHEMA IF NOT EXISTS PURGE_SCHEMA_1")
        connection.execute("CREATE SCHEMA IF NOT EXISTS PURGE_SCHEMA_2")
        connection.commit()
        factory = ExasolObjectFactory()
        factory.purge_user_objects()
        with connection.execute("SELECT SCHEMA_NAME FROM SYS.EXA_DBA_SCHEMAS") as statement:
            remaining_schemas = [row[0] for row in statement]
            assert remaining_schemas == []
