from Component import FileSystemComponent

class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.components = []
        
    def get_name(self):
        return self.name()
    
    def get_size(self):
        return sum([component.get_size() for component in self.components])
    
    def add(self, component):
        self.components.append(component)
        
    def remove(self, component):
        self.components.remove(component)