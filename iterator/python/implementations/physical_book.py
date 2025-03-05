from interfaces.book import Book

class PhysicalBook(Book):
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

