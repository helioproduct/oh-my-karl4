from abc import abstractmethod, ABC


class StorageElement:

    def __init__(self, path: str, size: int):
        self.path = path
        self.size = size

    def get_size(self) -> int:
        return self.size

    def get_path(self) -> str:
        return self.path

    def __eq__(self, other):
        return self.__hash__() == other.__hash__() and self.get_size() == other.get_size()

    def __hash__(self):
        return self.get_path().__hash__()

    def __str__(self):
        return self.get_path() + ' ' + str(self.get_size())


class Directory(StorageElement):

    def __init__(self, path, size=0, content=None):
        super().__init__(path, size)
        if content is None:
            content = set()
        self.content = content

    def get_size(self):
        if len(self.content) == 0:
            return 0
        return sum([element.get_size() for element in self.content])

    def get_content(self):
        return self.content

    def add_element(self, element: StorageElement):
        self.content.add(element)


class File(StorageElement):

    def __init__(self, path, size=0):
        super().__init__(path, size)

    def get_size(self):
        return self.size


class Storage(ABC):

    @abstractmethod
    def index_storage(self):
        pass

    @abstractmethod
    def get_storage_size(self):
        pass

    @abstractmethod
    def get_free_space_size(self):
        pass


class ElementNotFoundException(Exception):

    def __init__(self, element: StorageElement):

        if element is File:
            self.message = 'FILE ' + element.get_path() + ' not found'
        elif element is Directory:
            self.message = 'DIRECTORY ' + element.get_path() + ' not found'
