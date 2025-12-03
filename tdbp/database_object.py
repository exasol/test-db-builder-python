from abc import ABC, abstractmethod

from tdbp.database_object_listener import DatabaseObjectListener


class DatabaseObject(ABC):
    def __init__(self, listener: DatabaseObjectListener, name: str):
        self.name = name
        self.listener = listener

    @abstractmethod
    def fully_qualified_name(self) -> str:
        pass