from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from exasol.tdbp.database_object_listener import DatabaseObjectListener


class DatabaseObject(ABC):
    """
    Abstract base class for database objects.

    This class serves as a blueprint for defining database objects with a name
    and an associated listener that observes events.

    Attributes:
        name (str): The name of the database object.
        listener (DatabaseObjectListener): The listener that observes this database object.
    """

    def __init__(self, listener: DatabaseObjectListener, name: str):
        self.name = name
        self.listener = listener

    @abstractmethod
    def fully_qualified_name(self) -> str:
        """
        Retrieves the fully qualified name representation of an entity.

        Returns:
            str: The fully qualified name representation of the entity.
        """
