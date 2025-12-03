from tdbp.database_object import DatabaseObject
from tdbp.database_object_listener import DatabaseObjectListener
from tdbp.table import Table


class Schema(DatabaseObject):
    def __init__(self, listener: DatabaseObjectListener, schema_name: str):
        super().__init__(listener, schema_name)
        
    def create_table(self, table_name: str, **columns):
        table = Table(self.listener, table_name, self, **columns)
        self.listener.on_create(table)
        return table
