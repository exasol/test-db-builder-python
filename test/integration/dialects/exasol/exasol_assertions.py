from __future__ import annotations
from typing import Self, Any
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

    def returns(self, *expected):
        expected_rows = self.__normalize_row_list(expected)
        with self.connection.execute(self.sql) as statement:
            actual = statement.fetchall()
            assert actual == expected_rows, f"Expected {expected_rows}, got {actual}"

    def __normalize_row_list(self, expected: tuple[Any, ...]) -> list[list]:
        if len(expected) == 1:
            if isinstance(expected[0], list):
                expected_rows = expected[0]
            elif not isinstance(expected[0], tuple):
                expected_rows = [(expected[0],)]
            else:
                expected_rows = [[expected]]
        else:
            expected_rows = [expected]
        return expected_rows