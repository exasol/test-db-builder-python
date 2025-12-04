from pyexasol import ExaConnection

from exasol.tdbp.dialects.database_object_factory import DatabaseObjectFactory
from exasol.tdbp.dialects.exasol.exasol_immediate_database_object_writer import ExasolImmediateDatabaseObjectWriter


class ExasolObjectFactory(DatabaseObjectFactory):
    def __init__(self, connection: ExaConnection):
        super().__init__("Exasol", ExasolImmediateDatabaseObjectWriter(connection))

    def purge_user_objects(self):
        self.listener.purge_user_objects()