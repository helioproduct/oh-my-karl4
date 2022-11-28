from abc import abstractmethod, ABC


class StorageElement:

    def __init__(self, name: str, size: int, element_type: str) -> None:
        self.name = name
        self.size = size
        self.type = element_type

    def get_size(self) -> int:
        return self.size

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type


class Storage(ABC):

    def __init__(self, name, size, content=None):
        if content is None:
            content = set()
        self.name = name
        self.size = size
        self.content = content

    @abstractmethod
    def get_total_size(self):
        pass

    @abstractmethod
    def get_used_space_size(self):
        pass

    @abstractmethod
    def get_free_space_size(self):
        pass
