.. _user_guide:

User Guide
=============================================


Test Database Builder for Python (TDBP) is a testing library designed to make database integration testing easier and more maintainable. It provides a fluent interface for setting up test data and cleaning up test databases between test cases.

TDBP follows the principle that each test should be responsible for setting up exactly the data it needs, no more, no less. This approach leads to more maintainable tests that are easier to understand and modify.

The Challenge
-------------

Integration tests with databases are often tedious to write and even harder to review.

A test style that is both wide-spread and a maintenance nightmare is to create one large database and run all test against the same data.

Worse yet, some test frameworks have tests that write data and build on each other.

There are a number of things wrong with these approach, too many to list them all, so here are the top five:

1. One large test set means noone can remember exactly what is in it.
2. Reviewers and maintainers have to jump between the code that creates the test dataset and the test constantly.
3. If you have writing tests, they destroy your test setup.
4. Test cases are not independent — you cannot switch their order or run them in isolation.
5. The test cases are tightly coupled — change one place, expect to have to change a couple others.

How TDBP Solves These Issues
----------------------------

The main purpose of TDBP is to reduce the boilerplate for test data setup to a minimum, so that developers can afford to have each single file prepare just the data it needs.

Clean-up is even more convenient. With TDBP you can have a fixture clean your test database before each test case. This gives you a clean slate each time and prevents tests that write data to interfere with other tests.

Using TDBP
----------

Preparing Test Fixtures
-----------------------

TDBP is designed to work with pytest fixtures. You'll need to set up a few basic fixtures to get started:

1. A connection fixture that manages the database connection
2. A factory fixture that provides methods to create database objects
3. An assertions fixture for verifying database state

Here's a typical fixture setup:

.. code-block:: python

    @pytest.fixture(scope="module")
    def connection():
        with connect() as connection:
            yield connection

    @pytest.fixture
    def factory(connection):
        factory = DatabaseObjectFactory(connection)
        factory.purge_user_objects()  # Clean up before each test
        return factory

    @pytest.fixture()
    def db_assert():
        with DatabaseAssertions() as assertions:
            yield assertions

The connection fixture has module scope to avoid creating too many connections, while the factory fixture runs for each test to ensure a clean database state.

Creating Database Objects
-------------------------

Preparing test data in a database usually happens in two steps. First you create the necessary database objects, then you populate them with data.

Example: Creating and Populating a Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a simple example of how to create a schema and table using TDBP:

.. code-block:: python

    def test_database_setup(factory, db_assert):
        # Prepare the required schema and table...
        schema = factory.create_schema("EXAMPLE_SCHEMA")
        table = schema.create_table("EXAMPLE_TABLE",
                                  ID="DECIMAL(12,0)",
                                  NAME="VARCHAR(255)")

        # ... populate it with data...
        table.insert(1, "Test record").insert(2, "Another record")
        
        # ... run the code under test here...
        # ... then validate the results.

This example demonstrates several key features of TDBP:

* The ``factory.create_schema()`` method creates a new schema in the database
* ``schema.create_table()`` creates a table with the specified columns and data types
* The fluent interface allows for method chaining with ``insert()``

Example: Bulk Insert
~~~~~~~~~~~~~~~~~~~~

Even in a functional test you sometimes need a couple of records in the same table. To make the code more compact, TDBP offers a bulk insert.

.. code-block:: python

    def test_bulk_insert(factory, db_assert):
        # Create schema and table
        # ...
        # Insert multiple rows at once
        table.insert_all(
            [1, "Alice Smith"],
            [2, "Bob Johnson"],
            [3, "Carol Williams"]
        )

Database Dialects
-----------------

TDBP is written database agnostic but comes with the concept of dialects. A dialect is an adapter for a specific database like Exasol or MariaDB.

This is especially useful if your integration test requires testing more than one database at a time. Imagine testing an ETL process between two databases for example.

Dialects also allow implementing TDBP support for objects that only a certain database has. Exasol has UDFs and a corresponding SQL syntax that needs to be abstracted.

When Objects and Data get Written
---------------------------------

When you create database object or populate them with data, events are sent to a listner that can act on them.

A typical listener is a database object writer, that takes care of persisting the objects you create with TDBP.

Since in an integration test case you usually expect everything to be present in the database by the time you reach the point in the test case where you exercises your production, TDBP comes with a writer that persists the objects and data immediately (e.g., the `ExasolImmediateDatabaseObjectWriter`).

