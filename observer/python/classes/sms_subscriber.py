from interfaces.observer import Observer

class SMSSubscriber(Observer):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, news):
        """Notificación por SMS"""
        print(f"Enviando SMS al {self.phone_number}: Noticias - {news}")