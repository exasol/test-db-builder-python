from __future__ import annotations
from typing import TYPE_CHECKING

from tdbp.database_object import DatabaseObject
from tdbp.database_object_listener import DatabaseObjectListener

if TYPE_CHECKING:
    from tdbp.schema import Schema


class Table(DatabaseObject):
    def __init__(self, listener: DatabaseObjectListener,  table_name: str, schema: Schema, **columns):
        DatabaseObject.__init__(self, listener, table_name)
        self.schema = schema
        self.columns = columns
