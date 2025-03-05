package iterator.java.implementations;

import java.util.List;

import iterator.java.interfaces.Book;
import iterator.java.interfaces.Iterator;

public class PhysicalBookIterator implements Iterator {
    private List<Book> books;
    private int position = 0;

    public PhysicalBookIterator(List<Book> books) {
        this.books = books;
    }

    @Override
    public Book first() {
        position = 0;
        return currentItem();
    }

    @Override
    public void next() {
        position++;
    }

    @Override
    public boolean isDone() {
        return position >= books.size();
    }

    @Override
    public Book currentItem() {
        return isDone() ? null : books.get(position);
    }
}