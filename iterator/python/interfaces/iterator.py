from abc import ABC, abstractmethod
from typing import Optional
from interfaces.book import Book

class Iterator(ABC):
    @abstractmethod
    def first(self) -> Optional[Book]:
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def current_item(self) -> Optional[Book]:
        pass