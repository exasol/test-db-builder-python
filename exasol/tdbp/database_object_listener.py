from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from typing import TYPE_CHECKING

from exasol.tdbp.table import Table

if TYPE_CHECKING:
    from exasol.tdbp.database_object import DatabaseObject


class DatabaseObjectListener(ABC):
    """
    Abstract Base Class for listening to database object events.

    This class serves as a base class for defining listeners that monitor various
    events on database objects, such as object creation or data insertion. It acts
    as a blueprint for implementing specific behaviors during these events.

    The main purpose is to allow different strategies for writing database objects,
    for example, immediately or in batches.
    """

    @abstractmethod
    def purge_user_objects(self) -> None:
        """
        Abstract method to purge user-related objects.

        It is intended to clean up or remove user-specific objects or related data
        to ensure provide a clean database for testing.
        """

    @abstractmethod
    def on_create(self, database_object: DatabaseObject) -> None:
        """
        Handles database object creation events.

        Args:
            database_object: The database object that was created.
        """

    @abstractmethod
    def on_insert(self, table: Table, values: list):
        """
        Handles the event triggered when a new record is inserted into the table.

        Args:
            table (Table): The table where the record is being inserted.
            values (list): A list containing the values of the new record.
        """
        pass

    @abstractmethod
    def on_insert_all(self, table: Table, values: list[list]):
        """
        Handles bulk insertion of data into a table.

        Args:
            table (Table): The table into which the data will be inserted.
            values (list[list]): A list of lists containing the rows of data to
                be inserted.
        """
