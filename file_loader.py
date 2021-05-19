from abc import ABC, abstractmethod
import json


class FileLoad(ABC):

    @abstractmethod
    def load(self, filepath):
        pass


class JSONLoad(FileLoad):

    def load(self, filepath):
        with open(filepath) as file:
            data = json.load(file)
        return data
