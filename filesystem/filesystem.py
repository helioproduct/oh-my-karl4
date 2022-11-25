from typing import List


class StorageElement:

    def __init__(self, name) -> None:
        self.name = name
    
    
    def get_name(self):
        return self.name


    def get_size(self):
        return self.size


class Folder(StorageElement):

    def __init__(self, name, content) -> None:
        super().__init__(name)
        self.content = content


    def get_size(self):
        return sum([element.get_size() for element in self.content])


class File(StorageElement):

    def __init__(self, name, size=0, extension=None) -> None:
        super().__init__(name)
        self.size = size
        self.extension = extension


    def get_extension(self):
        return self.extension


class Storage():    

    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content


    def get_total_size(self) -> int:
        return self.size


    def get_size_used(self) -> int:
        return sum([element.get_size() for element in self.content])


    def get_free_size(self) -> int:
        return self.get_total_size() - self.get_size_used()
