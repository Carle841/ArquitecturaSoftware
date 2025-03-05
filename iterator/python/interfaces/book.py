from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass