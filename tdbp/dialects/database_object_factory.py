from tdbp.database_object_listener import DatabaseObjectListener
from tdbp.schema import Schema


class DatabaseObjectFactory:
    """
    Factory class for creating database objects.

    This class provides a way to construct various database objects, such
    as schemas, and ensures proper event notifications are sent when these
    objects are created.

    The purpose of the injected listeners is to write objects to the database
    with different strategies. Depending on the injected listener, the objects
    are written immediately or in batches.

    Args:
        name (str): The name of the factory instance.
        listener (DatabaseObjectListener): A listener to handle events triggered
            during the creation of database objects.
    """

    def __init__(self, name: str, listener: DatabaseObjectListener):
        self.name = name
        self.listener = listener

    def create_schema(self, name: str) -> Schema:
        """
        Creates a new schema with the given name and triggers the creation listener.

        Args:
            name: The name of the schema to be created.

        Returns:
            A Schema instance representing the newly created schema.
        """
        schema = Schema(self.listener, name)
        self.listener.on_create(schema)
        return schema
