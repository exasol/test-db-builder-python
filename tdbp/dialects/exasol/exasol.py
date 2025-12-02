from tdbp.dialects.dialect import Dialect
from tdbp.dialects.exasol.exasol_immediate_database_object_writer import ExasolImmediateDatabaseObjectWriter


class Exasol(Dialect):
    def __init__(self):
        Dialect.__init__(self, "Exasol", ExasolImmediateDatabaseObjectWriter())

    def purge_user_objects(self):
        self.writer.purge_user_objects()