from abc import ABC, abstractmethod
from document import Document, Resume, Report

# Clase creadora abstracta que declara el metodo factoryMethod
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass


    # Operacion que usa el factoryMethod
    def do_operation(self):
        document = self.create_document()
        document.open()
        document.save()
        return document
    
# Creador concreto para curriculum
class ResumeCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Resume()
        
# Creador concreto para reporte
class ReportCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Report()