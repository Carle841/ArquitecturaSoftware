from abc import ABC, abstractmethod

class Soporte(ABC):
    def __init__(self):
        self.proximo_nivel = None

    def establecer_proximo_nivel(self, proximo_nivel):
        self.proximo_nivel = proximo_nivel

    @abstractmethod
    def manejar_solicitud(self, solicitud):
        pass