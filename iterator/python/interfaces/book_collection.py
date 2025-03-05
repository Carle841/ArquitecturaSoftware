from abc import ABC, abstractmethod
from interfaces.iterator import Iterator

class BookCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass