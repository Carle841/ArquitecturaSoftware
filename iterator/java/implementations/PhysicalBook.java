package iterator.java.implementations;

import iterator.java.interfaces.Book;

public class PhysicalBook implements Book {
    private String title;
    private String author;

    public PhysicalBook(String title, String author) {
        this.title = title;
        this.author = author;
    }

    @Override
    public String getTitle() {
        return title;
    }

    @Override
    public String getAuthor() {
        return author;
    }
}

