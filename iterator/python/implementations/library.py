from interfaces.iterator import Iterator

class Library:
    @staticmethod
    def display_books(iterator: Iterator) -> None:
        book = iterator.first()
        while not iterator.is_done():
            print(f"Libro: {book.get_title()} - Autor: {book.get_author()}")
            iterator.next()
            book = iterator.current_item()