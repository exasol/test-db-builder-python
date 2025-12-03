import pytest

from tdbp.dialects.exasol.exasol_connection_factory import connect
from tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory


def test_create_schema(factory):
    schema = factory.create_schema("CREATE_SCHEMA_TEST")
    with connect() as connection:
        with connection.execute("""SELECT "SCHEMA_NAME" FROM "SYS"."EXA_DBA_SCHEMAS";""") as statement:
            rows = [row[0] for row in statement]
            assert schema.name in rows

def test_create_table(factory):
    schema = factory.create_schema("CREATE_TABLE_TEST")
    table = schema.create_table("CREATE_TABLE_TEST_TABLE", ID = "DECIMAL(12,0)", NAME = "VARCHAR(255)")
    with connect() as connection:
        with connection.execute(f"""SELECT "COLUMN_NAME", "COLUMN_TYPE"
            FROM "SYS"."EXA_ALL_COLUMNS"
            WHERE column_schema = '{schema.name}' AND "COLUMN_TABLE" = '{table.name}'"""
        ) as statement:
            rows = statement.fetchall()
            assert rows == [("ID", "DECIMAL(12,0)"), ("NAME", "VARCHAR(255) UTF8")]

@pytest.fixture
def factory():
    factory = ExasolObjectFactory()
    factory.purge_user_objects()
    return factory
