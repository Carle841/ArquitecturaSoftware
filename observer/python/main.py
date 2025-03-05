from classes.news_publisher import NewsPublisher
from classes.email_subscriber import EmailSubscriber
from classes.sms_subscriber import SMSSubscriber

def main():
    # Crear el publicador de noticias
    news_publisher = NewsPublisher()

    # Crear suscriptores
    email_sub1 = EmailSubscriber('usuario1@ejemplo.com')
    email_sub2 = EmailSubscriber('usuario2@ejemplo.com')
    sms_sub = SMSSubscriber('+1234567890')

    # Añadir suscriptores
    news_publisher.attach(email_sub1)
    news_publisher.attach(email_sub2)
    news_publisher.attach(sms_sub)

    # Publicar primera noticia
    news_publisher.publish_news('¡Gran evento acontece hoy!')

    # Desuscribir un observador
    news_publisher.detach(email_sub2)

    # Publicar segunda noticia
    news_publisher.publish_news('Actualización importante')

if __name__ == "__main__":
    main()