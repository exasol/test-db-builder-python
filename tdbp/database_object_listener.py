from __future__ import annotations
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

from tdbp.table import Table

if TYPE_CHECKING:
    from tdbp.database_object import DatabaseObject


class DatabaseObjectListener(ABC):
    @abstractmethod
    def purge_user_objects(self) -> None:
        pass

    @abstractmethod
    def on_create(self, database_object: DatabaseObject) -> None:
        pass

    @abstractmethod
    def on_insert(self, table: Table, values: list  ):
        pass
