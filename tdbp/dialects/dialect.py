from tdbp.DatabaseObjectWriter import DatabaseObjectWriter
from tdbp.schema import Schema


class Dialect:
    def __init__(self, name: str, writer: DatabaseObjectWriter):
        self.name = name
        self.writer = writer

    def create_schema(self, name: str) -> Schema:
        schema = Schema(name)
        self.writer.write(schema)
        return schema