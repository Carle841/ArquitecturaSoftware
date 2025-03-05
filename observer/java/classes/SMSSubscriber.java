package observer.java.classes;

import observer.java.interfaces.Observer;

public class SMSSubscriber implements Observer {
    private String phoneNumber;

    public SMSSubscriber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    @Override
    public void update(String news) {
        System.out.println("Enviando SMS al " + phoneNumber + ": Noticias - " + news);
    }
}
