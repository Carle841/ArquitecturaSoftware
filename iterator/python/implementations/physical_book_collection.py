from typing import List
from interfaces.book_collection import BookCollection
from interfaces.iterator import Iterator
from interfaces.book import Book
from implementations.physical_book_iterator import PhysicalBookIterator

class PhysicalBookCollection(BookCollection):
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def create_iterator(self) -> Iterator:
        return PhysicalBookIterator(self._books)
