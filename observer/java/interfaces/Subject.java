package observer.java.interfaces;

public interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notify(String news);
}
