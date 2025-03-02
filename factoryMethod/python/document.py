from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
#Implementacion concreta de Document
class Resume(Document):
    def open(self):
        print("Abriendo curriculum")
    
    def save(self):
        print("Guardadndo curriculum")
        
# Otra implementacion concreta de Document
class Report(Document):
    def open(self):
        print("Abriendo reporte")
    
    def save(self):
        print("Guardadndo reporte")