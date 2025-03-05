from typing import List, Optional
from interfaces.iterator import Iterator
from interfaces.book import Book

class PhysicalBookIterator(Iterator):
    def __init__(self, books: List[Book]):
        self._books = books
        self._position = 0

    def first(self) -> Optional[Book]:
        self._position = 0
        return self.current_item()

    def next(self) -> None:
        self._position += 1

    def is_done(self) -> bool:
        return self._position >= len(self._books)

    def current_item(self) -> Optional[Book]:
        return None if self.is_done() else self._books[self._position]