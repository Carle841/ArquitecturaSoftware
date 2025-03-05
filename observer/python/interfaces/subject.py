from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        """Añadir un observador"""
        pass

    @abstractmethod
    def detach(self, observer):
        """Eliminar un observador"""
        pass

    @abstractmethod
    def notify(self):
        """Notificar a todos los observadores"""
        pass