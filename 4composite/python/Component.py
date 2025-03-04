from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass   
    
    @abstractmethod
    def add(self, component):
        pass
    
    @abstractmethod
    def remove(self, component):
        pass
    