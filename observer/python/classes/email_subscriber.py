from interfaces.observer import Observer

class EmailSubscriber(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, news):
        """Notificación por correo electrónico"""
        print(f"Enviando email a {self.email}: Noticias - {news}")