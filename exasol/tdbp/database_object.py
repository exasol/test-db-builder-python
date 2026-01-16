from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from typing import TYPE_CHECKING

from exasol.tdbp.dialects.exasol.exasol_identifier import ExasolIdentifier

if TYPE_CHECKING:
    from exasol.tdbp.database_object_listener import DatabaseObjectListener


class DatabaseObject(ABC):
    """
    Abstract base class for database objects.

    This class serves as a blueprint for defining database objects with a name
    and an associated listener that observes events.

    Attributes:
        listener (DatabaseObjectListener): The listener that observes this database object.
        name (str): The name of the database object.
    """

    def __init__(self, listener: DatabaseObjectListener, name: str):
        self.listener = listener
        self.identifier = ExasolIdentifier.of(name)

    @abstractmethod
    def fully_qualified_name(self) -> str:
        """
        Retrieves the fully qualified name representation of an entity.

        Returns:
            str: The fully qualified name representation of the entity.
        """
