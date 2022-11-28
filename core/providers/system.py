from core.filesystem.storage import Storage
import os


class SystemStorage(Storage):

    def __init__(self, name, size):
        super().__init__(name, size)

    def __init__(self, path_to_storage: str):
        passs


    def get_total_size(self):
        pass

    def get_used_space_size(self):
        pass

    def get_free_space_size(self):
        pass


print(os.getcwd())
os.chdir('/home/helio/Desktop/')
print(os.getcwd())
