package observer.java;

import observer.java.classes.NewsPublisher;
import observer.java.classes.EmailSubscriber;
import observer.java.classes.SMSSubscriber;

public class Main {
    public static void main(String[] args) {
        // Crear el publicador de noticias
        NewsPublisher newsPublisher = new NewsPublisher();

        // Crear suscriptores
        EmailSubscriber emailSub1 = new EmailSubscriber("usuario1@ejemplo.com");
        EmailSubscriber emailSub2 = new EmailSubscriber("usuario2@ejemplo.com");
        SMSSubscriber smsSub = new SMSSubscriber("+1234567890");

        // Añadir suscriptores
        newsPublisher.attach(emailSub1);
        newsPublisher.attach(emailSub2);
        newsPublisher.attach(smsSub);

        // Publicar primera noticia
        newsPublisher.publishNews("¡Gran evento acontece hoy!");

        // Desuscribir un observador
        newsPublisher.detach(emailSub2);

        // Publicar segunda noticia
        newsPublisher.publishNews("Actualización importante");
    }
}
