from filesystem.storage import *
import os
import psutil


class SystemStorageManager(StorageManager, ABC):

    def __init__(self, name: str, source_path: str):
        self.root_directory = Directory(name, 0)
        self.source_path = source_path

    def get_source_path(self) -> str:
        return self.source_path

    def index_directory(self, path: str, directory: Directory):
        os.chdir(path)
        names = os.listdir()

        for name in names:
            el = None
            absolute_path = path + name
            size = os.stat(absolute_path).st_size

            if os.path.isfile(absolute_path):
                el = File(name, size)
            elif os.path.isdir(absolute_path):
                el = Directory(name, 0)
                self.index_directory(path + name + '/', el)

            directory.add_element(el)

    def index_storage(self):
        self.index_directory(self.source_path, self.root_directory)

    def get_storage_size(self) -> int:
        return psutil.disk_usage(self.source_path)[2]

    def get_free_space_size(self) -> int:
        return self.get_storage_size() - self.get_used_size()

    def get_used_size(self):
        return self.root_directory.get_size()


# storage_manager = SystemStorageManager('local', '/home/helio/Desktop/Storage/')
# storage_manager.index_storage()
# print(storage_manager.get_used_size())
# print(storage_manager.root_directory.get_name())


