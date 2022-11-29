from .storage import Storage
from typing import List


class FileSystem:

    def __init__(self, storages: List[Storage], mount_point: str):
        self.storages = storages
        self.mount_point = mount_point

    def get_mount_point(self) -> str:
        return self.mount_point

    def ls(self, path: str):
        pass

    def mkdir(self, path: str):
        pass

    def rm(self, path: str):
        pass

    def rmdir(self, path: str):
        pass
