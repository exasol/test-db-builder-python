# Unreleased

This is the initial release of the "Test Database Builder for Python (TDBP)" project.

The release offers support for the Exasol dialect, meaning that you can use TDBP to generate test data for Exasol databases.

Features:

1. Create schemas and tables in Exasol databases
2. Insert data into tables
3. Fluent programming interface

Here is a short example. First, create the pytest fixture that provides the Exasol connection and the ExasolObjectFactory.

```python
@pytest.fixture(scope="module")
def connection():
    with connect() as connection:
        yield connection

@pytest.fixture
def factory(connection):
    factory = ExasolObjectFactory(connection)
    factory.purge_user_objects()  # Clean slate for each test
    return factory
```

With that done, the test preparation gets very compact.

```python
    def test_insert_customers(factory):
        # Prepare the test database
        schema = factory.create_schema("SALES")
        table = schema.create_table("CUSTOMERS",
            ID="DECIMAL(12,0)", NAME="VARCHAR(255)")
        table.insert(1, "Alice").insert(2, "Bob")

        # Execute your test
        # ...

        # Assert the results
        # ...
```

## Refactoring

* #1: Added MIT license and security policy
* #3: Transformed project to comply with the standard layout of Exasol's Python projects by adding the Exasol Python Toolbox
* #12: Removed unused `Config` class from `noxconfig.py`

## Features

* #3: Basic support for Exasol
