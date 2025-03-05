package iterator.java;

import java.util.Iterator;

import iterator.java.implementations.Library;
import iterator.java.implementations.PhysicalBook;
import iterator.java.implementations.PhysicalBookCollection;

public class Main {
    public static void main(String[] args) {
        PhysicalBookCollection collection = new PhysicalBookCollection();
        collection.addBook(new PhysicalBook("Don Quijote", "Miguel de Cervantes"));
        collection.addBook(new PhysicalBook("Cien Años de Soledad", "Gabriel García Márquez"));

        iterator.java.interfaces.Iterator iterator = collection.createIterator();
        Library.displayBooks(iterator);
    }
}
