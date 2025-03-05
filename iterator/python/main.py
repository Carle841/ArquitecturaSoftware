from implementations.physical_book import PhysicalBook
from implementations.physical_book_collection import PhysicalBookCollection
from implementations.library import Library

def main():
    collection = PhysicalBookCollection()
    collection.add_book(PhysicalBook("Don Quijote", "Miguel de Cervantes"))
    collection.add_book(PhysicalBook("Cien Años de Soledad", "Gabriel García Márquez"))

    iterator = collection.create_iterator()
    Library.display_books(iterator)

if __name__ == "__main__":
    main()