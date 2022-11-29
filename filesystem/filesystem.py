from .storage import Storage
from typing import List


class FileSystem:

    def __init__(self, storages: List[Storage]):
        self.storages = storages

    def ls(self, path: str):
        pass

    def mkdir(self, path: str):
        pass

    def rm(self, path: str):
        pass

    def rmdir(self, path: str):
        pass

