import pytest

from tdbp.dialects.exasol.exasol_connection_factory import connect
from tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory
from test.integration.dialects.exasol.exasol_assertions import ExasolAssertions


def test_create_schema(factory, db_assert):
    schema = factory.create_schema("CREATE_SCHEMA_TEST")
    (db_assert.assert_query(
        f"""SELECT "SCHEMA_NAME"
            FROM "SYS"."EXA_DBA_SCHEMAS"
            WHERE "SCHEMA_NAME" = '{schema.name}'""")
     .returns([(schema.name,)]))


def test_create_table(factory, db_assert):
    schema = factory.create_schema("CREATE_TABLE_TEST")
    table = schema.create_table("CREATE_TABLE_TEST_TABLE", ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
    (db_assert.assert_query(
        f"""SELECT "COLUMN_NAME", "COLUMN_TYPE"
            FROM "SYS"."EXA_ALL_COLUMNS"
            WHERE column_schema = '{schema.name}' AND "COLUMN_TABLE" = '{table.name}'"""
    )
     .returns([("ID", "DECIMAL(12,0)"), ("NAME", "VARCHAR(255) UTF8")]))


def test_single_row_insert(factory, db_assert):
    schema = factory.create_schema("INSERT_WITH_NAMED_COLUMNS_TEST")
    table = schema.create_table("INSERT_WITH_NAMED_COLUMNS_TEST_TABLE", ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
    table.insert(1, "Test")
    (db_assert.assert_query(
        f"""SELECT *
            FROM {table.fully_qualified_name()}
            ORDER BY "ID" ASC""")
     .returns([(1, "Test")]))


def test_chained_single_row_insert(factory, db_assert):
    schema = factory.create_schema("INSERT_WITH_NAMED_COLUMNS_TEST")
    table = schema.create_table("INSERT_WITH_NAMED_COLUMNS_TEST_TABLE", ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
    table.insert(1, "Test").insert(2, "Test2")
    (db_assert.assert_query(
        f"""SELECT *
            FROM {table.fully_qualified_name()}
            ORDER BY "ID" ASC""")
     .returns([(1, "Test"), (2, "Test2")]))


def test_multiple_row_insert(factory, db_assert):
    schema = factory.create_schema("INSERT_WITH_NAMED_COLUMNS_TEST")
    table = schema.create_table("INSERT_WITH_NAMED_COLUMNS_TEST_TABLE", ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
    table.insert_all([1, "Test"], [2, "Test2"], [3, "Test3"])
    (db_assert.assert_query(
        f"""SELECT *
             FROM {table.fully_qualified_name()}
             ORDER BY "ID" ASC""")
     .returns([(1, "Test"), (2, "Test2"), (3, "Test3")]))

def test_chained_multiple_row_insert(factory, db_assert):
    schema = factory.create_schema("INSERT_WITH_NAMED_COLUMNS_TEST")
    table = schema.create_table("INSERT_WITH_NAMED_COLUMNS_TEST_TABLE", ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
    table.insert(1, "Test").insert_all([2, "Test2"], [3, "Test3"]).insert(4, "Test4").insert_all([5, "Test5"], [6, "Test6"])
    (db_assert.assert_query(
        f"""SELECT *
             FROM {table.fully_qualified_name()}
             ORDER BY "ID" ASC"""
    ).returns([(1, "Test"), (2, "Test2"), (3, "Test3"), (4, "Test4"), (5, "Test5"), (6, "Test6")]))


@pytest.fixture
def factory(connection):
    factory = ExasolObjectFactory(connection)
    factory.purge_user_objects()
    return factory

@pytest.fixture(scope="module")
def connection():
    with connect() as connection:
        yield connection


@pytest.fixture()
def db_assert():
    with ExasolAssertions() as assertions:
        yield assertions
