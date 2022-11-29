from filesystem.storage import *
from pathlib import Path
import os
import psutil


def index_directory(path: str) -> Directory:
    directory = Directory(path, 0)

    path = Path(path)
    os.chdir(path)
    names = os.listdir()

    for name in names:
        element = None
        absolute_path = path.joinpath(name)
        size = os.stat(absolute_path).st_size

        if os.path.isfile(str(path)):
            element = File(str(absolute_path), size)

        elif os.path.isdir(path):
            element = index_directory(str(absolute_path))

        directory.add_element(element)

    return directory


class LocalStorage(Storage, ABC):

    def __init__(self, mount_point: str, source_path: str):
        self.mount_point = mount_point
        self.source_path = source_path
        self.root_directory = index_directory(source_path)
        # self.root_directory = Directory(mount_point, 0)

    def get_source_path(self) -> str:
        return self.source_path

    def index_directory(self, path: str, directory: Directory):
        path = Path(path)
        os.chdir(path)
        names = os.listdir()

        for name in names:
            el = None
            absolute_path = path.joinpath(name)
            size = os.stat(absolute_path).st_size

            if os.path.isfile(absolute_path):
                el = File(str(absolute_path), size)

            elif os.path.isdir(absolute_path):
                el = Directory(name, 0)
                # print(absolute_path.relative_to('/home/helio/Desktop/Storage'))
                self.index_directory(str(absolute_path), el)

            directory.add_element(el)

    def index_storage(self):
        self.index_directory(self.source_path, self.root_directory)

    def get_storage_size(self) -> int:
        return psutil.disk_usage(self.source_path)[2]

    def get_free_space_size(self) -> int:
        return self.get_storage_size() - self.get_used_size()

    def get_used_size(self):
        return self.root_directory.get_size()


storage_manager = LocalStorage('/local', '/home/helio/Desktop/Storage/')
storage_manager.index_storage()
