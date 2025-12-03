from __future__ import annotations
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tdbp.database_object import DatabaseObject


class DatabaseObjectListener(ABC):
    @abstractmethod
    def purge_user_objects(self) -> None:
        pass

    @abstractmethod
    def on_create(self, object: DatabaseObject) -> None:
        pass
