from tdbp.dialects.dialect import Dialect
from tdbp.dialects.exasol.exasol_immediate_database_object_writer import ExasolImmediateDatabaseObjectListener


class Exasol(Dialect):
    def __init__(self):
        super().__init__("Exasol", ExasolImmediateDatabaseObjectListener())

    def purge_user_objects(self):
        self.listener.purge_user_objects()