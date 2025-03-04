from Component import FileSystemComponent

class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size
    
    def add(self, component):
        raise Exception("Cannot add to a File")
    
    def remove(self, component):
        raise Exception("Cannot remove from a File")