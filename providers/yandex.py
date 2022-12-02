from filesystem.storage import *
from pathlib import Path


class YandexStorage(Storage, ABC):

    def __init__(self, mount_point: str, name: str, token: str):
        self.mount_point = mount_point
        self.name = name
        self.token = token

