package iterator.java.implementations;

import java.util.ArrayList;
import java.util.List;

import iterator.java.interfaces.BookCollection;
import iterator.java.interfaces.Iterator;
import iterator.java.interfaces.Book;

public class PhysicalBookCollection implements BookCollection {
    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
    }

    @Override
    public Iterator createIterator() {
        return new PhysicalBookIterator(books);
    }
}




