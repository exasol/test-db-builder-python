import pytest

from tdbp.dialects.exasol.exasol_connection_factory import connect
from tdbp.dialects.exasol.exasol import Exasol


def test_create_schema(auto_cleaned_connection):
    schema_name = "CREATE_SCHEMA_TEST"
    dialect = Exasol()
    dialect.create_schema(schema_name)
    with auto_cleaned_connection as connection:
        with connection.execute(f"SELECT SCHEMA_NAME FROM SYS.EXA_DBA_SCHEMAS") as statement:
            rows = statement.fetchall()
            assert (schema_name, ) in rows


@pytest.fixture
def auto_cleaned_connection():
    Exasol().purge_user_objects()
    return connect()