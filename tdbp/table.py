from __future__ import annotations
from typing import TYPE_CHECKING, Any

from tdbp.database_object import DatabaseObject

if TYPE_CHECKING:
    from tdbp.schema import Schema
    from tdbp.database_object_listener import DatabaseObjectListener


class Table(DatabaseObject):
    def __init__(self, listener: DatabaseObjectListener,  table_name: str, schema: Schema, **columns):
        DatabaseObject.__init__(self, listener, table_name)
        self.schema = schema
        self.columns = columns

    def fully_qualified_name(self) -> str:
        return f'"{self.schema.name}"."{self.name}"'

    def insert(self, *values: Any) -> Table:
        self.listener.on_insert(self, list(values))
        return self

    def insert_all(self, *values: Any) -> Table:
        self.listener.on_insert_all(self, list(values))
        return self
