package iterator.java.implementations;

import iterator.java.interfaces.Book;
import iterator.java.interfaces.Iterator;

// implementations/Library.java
public class Library {
    public static void displayBooks(Iterator iterator) {
        for (Book book = iterator.first(); !iterator.isDone(); iterator.next(), book = iterator.currentItem()) {
            System.out.println("Libro: " + book.getTitle() + " - Autor: " + book.getAuthor());
        }
    }
}
