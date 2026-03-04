from test.integration.dialects.exasol.exasol_assertions import ExasolAssertions

import pytest
import pyexasol

from exasol.pytest_backend import backend_aware_database_params

from exasol.tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory


@pytest.fixture
def connection(backend_aware_database_params):
    with pyexasol.connect(**backend_aware_database_params) as conn:
        yield conn


@pytest.fixture
def factory(connection):
    factory = ExasolObjectFactory(connection)
    factory.purge_user_objects()
    return factory


@pytest.fixture
def db_assert(connection):
    with ExasolAssertions(connection) as assertions:
        yield assertions
