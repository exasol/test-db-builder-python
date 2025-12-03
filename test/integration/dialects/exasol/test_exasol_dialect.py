import pytest

from tdbp.dialects.exasol.exasol_connection_factory import connect
from tdbp.dialects.exasol.exasol import Exasol


def test_create_schema(dialect):
    schema = dialect.create_schema("CREATE_SCHEMA_TEST")
    with connect() as connection:
        with connection.execute("SELECT schema_name FROM sys.exa_dba_schemas") as statement:
            rows = [row[0] for row in statement]
            assert schema.name in rows

def test_create_table(dialect):
    schema = dialect.create_schema("CREATE_TABLE_TEST")
    table = schema.create_table("CREATE_TABLE_TEST_TABLE", id = "INTEGER", name = "VARCHAR(255)")
    with connect() as connection:
        with connection.execute(f"SELECT column_name, column_type FROM sys.exa_all_columns WHERE column_schema = '{schema.name}' AND column_table = '{table.name}'") as statement:
            rows = statement.fetchall()
            assert rows == [("ID", "INTEGER"), ("NAME", "VARCHAR(255)")]

@pytest.fixture
def dialect():
    dialect = Exasol()
    dialect.purge_user_objects()
    return dialect
