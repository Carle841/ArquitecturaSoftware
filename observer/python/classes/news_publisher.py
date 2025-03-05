from interfaces.subject import Subject

class NewsPublisher(Subject):
    def __init__(self):
        self._observers = []
        self._latest_news = ""

    def attach(self, observer):
        """Añadir un nuevo observador"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Eliminar un observador"""
        self._observers.remove(observer)

    def notify(self):
        """Notificar a todos los observadores"""
        for observer in self._observers:
            observer.update(self._latest_news)

    def publish_news(self, news):
        """Publicar una noticia y notificar"""
        self._latest_news = news
        self.notify()