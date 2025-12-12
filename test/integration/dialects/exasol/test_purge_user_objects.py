from exasol.tdbp.dialects.exasol.exasol_connection_factory import connect


def test_purge_user_objects(factory, db_assert) -> None:
    with connect() as connection:
        connection.execute("CREATE SCHEMA IF NOT EXISTS PURGE_SCHEMA_1")
        connection.execute("CREATE SCHEMA IF NOT EXISTS PURGE_SCHEMA_2")
        connection.commit()
        factory.purge_user_objects()
        db_assert.assert_query(
            "SELECT SCHEMA_NAME FROM SYS.EXA_DBA_SCHEMAS"
        ).returns_empty()
