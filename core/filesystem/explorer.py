from .filesystem import FileSystem


class Explorer:

    def __init__(self, filesystem: FileSystem, current_path: str):
        self.filesystem = filesystem
        self.current_path = current_path

    def cd(self, path: str):
        pass

    def ls(self, path: str):
        pass

    def mkdir(self, path: str):
        pass

    def rm(self, path: str):
        pass

    def rmdir(self, path: str):
        pass
