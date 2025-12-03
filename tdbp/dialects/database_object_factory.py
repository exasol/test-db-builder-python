from tdbp.database_object_listener import DatabaseObjectListener
from tdbp.schema import Schema


class DatabaseObjectFactory:
    def __init__(self, name: str, listener: DatabaseObjectListener):
        self.name = name
        self.listener = listener

    def create_schema(self, name: str) -> Schema:
        schema = Schema(self.listener, name)
        self.listener.on_create(schema)
        return schema