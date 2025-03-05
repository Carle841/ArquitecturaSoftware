package observer.java.classes;

import observer.java.interfaces.Observer;

public class EmailSubscriber implements Observer {
    private String email;

    public EmailSubscriber(String email) {
        this.email = email;
    }

    @Override
    public void update(String news) {
        System.out.println("Enviando email a " + email + ": Noticias - " + news);
    }
}
