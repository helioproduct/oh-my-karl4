from filesystem.storage import *
import os
import psutil


# TODO: index folder mehtod implement
class SystemStorageManager(StorageManager, ABC):

    def __init__(self, mount_point: str, source_path: str):
        self.mount_point = mount_point
        self.source_path = source_path
        self.storage = Storage()
        self.index_storage()

    def get_source_path(self) -> str:
        return self.source_path

    def index_storage(self):
        os.chdir(self.source_path)
        names = os.listdir()
        for name in names:
            element = None
            absolute_path = self.get_source_path() + name
            size = os.stat(absolute_path).st_size

            if os.path.isfile(absolute_path):
                element = File(name, size)
            elif os.path.isdir(absolute_path):
                element = Directory(name, size)

            self.storage.add_element(element)

    def get_storage_size(self) -> int:
        return psutil.disk_usage(self.mount_point)[2]

    def get_free_space_size(self) -> int:
        return self.get_storage_size() - self.__calculate_used_size()

    def __calculate_used_size(self):
        return sum([element.get_size() for element in self.storage.content])

storage_manager = SystemStorageManager('/', '/home/helio/Desktop/Storage/')

