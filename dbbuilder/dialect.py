from dbbuilder.schema import Schema


class Dialect:
    def __init__(self, name: str) -> Dialect:
        self.name = name

    def create_schema(self, name: str) -> Schema:
        return Schema(name)