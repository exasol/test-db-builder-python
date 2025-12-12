from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
)

from typing_extensions import override

from exasol.tdbp.database_object import DatabaseObject

if TYPE_CHECKING:
    from exasol.tdbp.database_object_listener import DatabaseObjectListener
    from exasol.tdbp.schema import Schema


class Table(DatabaseObject):
    """
    Represents a database table.

    This class models a table within a database. It supports schema association,
    defining columns, and provides methods for inserting records into the table.

    Attributes:
        schema (Schema): The schema to which this table belongs.
        columns (dict): A dictionary defining the columns of the table.
    """

    def __init__(
        self,
        listener: DatabaseObjectListener,
        table_name: str,
        schema: Schema,
        **columns,
    ):
        DatabaseObject.__init__(self, listener, table_name)
        self.schema = schema
        self.columns = columns

    @override
    def fully_qualified_name(self) -> str:
        return f'"{self.schema.identifier}"."{self.identifier}"'

    def insert(self, *values: Any) -> Table:
        """
        Inserts one or more values into the table and notifies the listener about the operation.

        Args:
            *values: Arbitrary number of values to be inserted into the table. The type
                of each value is determined by the table's definition.

        Returns:
            Table: The current table instance for fluent method chaining.
        """
        self.listener.on_insert(self, list(values))
        return self

    def insert_all(self, *values: Any) -> Table:
        """
        Inserts all provided values into the table and notifies the listener.

        Args:
            *values: Any
                The values to be inserted into the table.

        Returns:
             Table: The current table instance for fluent method chaining.
        """
        self.listener.on_insert_all(self, list(values))
        return self
