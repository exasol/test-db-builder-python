from __future__ import annotations
from typing import Self
from types import TracebackType

from tdbp.dialects.exasol.exasol_connection_factory import connect


class ExasolAssertions:
    def __init__(self):
        self.connection = None

    def __enter__(self) -> Self:
        self.connection = connect()
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_tb: TracebackType | None
                 ) -> bool:
        if self.connection:
            self.connection.close()
        return False

    def assert_query(self, sql: str):
        return QueryAssertion(self.connection, sql)


class QueryAssertion:
    def __init__(self, connection, sql: str):
        self.connection = connection
        self.sql = sql

    def returns(self, expected_rows: list):
        with self.connection.execute(self.sql) as statement:
            actual = statement.fetchall()
            assert actual == expected_rows, f"Expected {expected_rows}, got {actual}"
