from tdbp.dialects.database_object_factory import DatabaseObjectFactory
from tdbp.dialects.exasol.exasol_immediate_database_object_writer import ExasolImmediateDatabaseObjectWriter


class ExasolObjectFactory(DatabaseObjectFactory):
    def __init__(self):
        super().__init__("Exasol", ExasolImmediateDatabaseObjectWriter())

    def purge_user_objects(self):
        self.listener.purge_user_objects()