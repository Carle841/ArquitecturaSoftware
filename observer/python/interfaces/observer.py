from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, news):
        """Método para recibir actualizaciones"""
        pass