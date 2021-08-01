from abc import ABC, abstractmethod


class DB(ABC):
    def __init__(self):
        self.conn = None
        self.cursor = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def kill(self):
        self.conn = None
        self.cursor = None

