Test Database Builder Python (TDDB)
============================

Test Database Builder Python (TDDB) is a lightweight framework that simplifies database integration testing by providing a fluent API for creating test database objects and test data.

It helps developers write cleaner, more maintainable database integration tests by eliminating boilerplate code and providing a consistent way to set up test data.

TDDB promotes the concept of disposable test setups. The compact code encourages keeping each test independent by having it create its own test dataset.
This also makes reviews much easier, since setup execution and assertions are close to each other.

Please note that TDDB aims at functional tests, where the amount of data required for each test is usually small.
If you need to test with large amounts of data, TDDB is not the right approach. It is especially ill-suited for performance testing.

This project is inspired by Exasol's Test Database Builder for Java (https://github.com/exasol/test-db-builder-java).

Target Audience
---------------

TDDB is designed for:

- Software developers writing database integration tests
- QA engineers automating database tests
- Database developers testing stored procedures and functions
- Anyone needing to create temporary test database objects and data


.. tip:: We recommend using TDDB when:

    - You need to create temporary database objects for functional testing
    - You want to isolate tests from each other
    - You need to repeatedly set up and tear down test data
    - You want to make your database tests more readable, maintainable and easy to review

.. warning:: **Do not** use TDDB in any of the situations below:

    - Production data management
    - Performance testing (use dedicated tools instead)
    - Managing persistent database objects
    - Complex data modeling (use proper database migration tools)


Quick Start
-------------

We recommend to make the object factory a fixture in your integration test and purge the database before each test. This ensures test isolation.

.. code-block:: python3

    @pytest.fixture(scope="module")
    def connection():
        with connect() as connection:
            yield connection
    
    @pytest.fixture
    def factory(connection):
        factory = ExasolObjectFactory(connection)
        factory.purge_user_objects()  # Clean slate for each test
        return factory

With that done, the test preparation gets very compact.

.. code-block:: python3

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

Information for Users
---------------------

* 📖 `User Guide <docs/user_guide.rst>`_: Detailed instructions on using TDDB including examples and best practices