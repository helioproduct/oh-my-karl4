from filesystem.storage import *
from pathlib import Path
import os
import psutil


class LocalStorage(Storage, ABC):

    # mount_point: where Storage located
    # source_path: where real Storage located
    def __init__(self, mount_point: str, name: str, source_path: str):
        self.mount_point = mount_point
        self.name = name
        self.source_path = source_path
        self.root_directory = Directory(source_path + '/' + name, 0)
        self.index_storage()

    def _get_source_path(self) -> str:
        return self.source_path

    def get_content(self):
        return self.root_directory.get_content()

    def index_directory(self, path: str, directory: Directory):
        path = Path(path)
        os.chdir(path)
        names = os.listdir()

        for name in names:
            element = None
            absolute_path = path.joinpath(name)
            size = os.stat(absolute_path).st_size

            relative_path = Path(self.name)
            relative_path = relative_path.joinpath(absolute_path.relative_to(self.source_path))

            if os.path.isfile(absolute_path):
                element = File(str(relative_path), size)
            elif os.path.isdir(absolute_path):
                element = Directory(str(relative_path), 0)
                self.index_directory(str(absolute_path), element)

            directory.add_element(element)

    def index_storage(self):
        self.index_directory(self.source_path, self.root_directory)

    def get_storage_size(self) -> int:
        return psutil.disk_usage(self.source_path)[2]

    def get_free_space_size(self) -> int:
        return self.get_storage_size() - self.get_used_size()

    def get_used_size(self):
        return self.root_directory.get_size()

    def get_real_path(self, element: StorageElement):
        source_path = Path(self._get_source_path())
        local_path = Path(element.get_path()).relative_to(self.name)
        return source_path.joinpath(local_path)
