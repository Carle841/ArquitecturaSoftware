package iterator.java.interfaces;

public interface Iterator {
    Book first();
    void next();
    boolean isDone();
    Book currentItem();
}
