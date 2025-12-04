import pytest

from exasol.tdbp.dialects.exasol.exasol_connection_factory import connect
from exasol.tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory
from test.integration.dialects.exasol.exasol_assertions import ExasolAssertions


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
