import abc
from abc import ABC, abstractmethod

class ICache(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get(self, key: str) -> str: ...
    @abstractmethod
    def set(self, key: str, value: str, expire: int): ...
