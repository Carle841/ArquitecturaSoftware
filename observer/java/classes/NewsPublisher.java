package observer.java.classes;

import observer.java.interfaces.Subject;
import observer.java.interfaces.Observer;
import java.util.ArrayList;
import java.util.List;

public class NewsPublisher implements Subject {
    private List<Observer> observers;
    private String latestNews;

    public NewsPublisher() {
        this.observers = new ArrayList<>();
    }

    @Override
    public void attach(Observer observer) {
        if (!observers.contains(observer)) {
            observers.add(observer);
        }
    }

    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notify(String news) {
        for (Observer observer : observers) {
            observer.update(news);
        }
    }

    public void publishNews(String news) {
        this.latestNews = news;
        notify(latestNews);
    }
}
