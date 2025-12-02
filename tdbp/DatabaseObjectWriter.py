from abc import ABC, abstractmethod

from tdbp.schema import Schema


class DatabaseObjectWriter(ABC):
    @abstractmethod
    def write(self, schema: Schema) -> None:
        pass

    @abstractmethod
    def purge_user_objects(self) -> None:
        pass