from typing import *
import abc
from abc import ABC, abstractmethod
from lark_oapi.core import T as T
from typing import Any

class IEventProcessor(ABC, Generic[T], metaclass=abc.ABCMeta):
    @abstractmethod
    def type(self) -> Type[T]: ...
    @abstractmethod
    def do(self, data: T) -> None: ...

class ICallBackProcessor(ABC, Generic[T], metaclass=abc.ABCMeta):
    @abstractmethod
    def type(self) -> Type[T]: ...
    @abstractmethod
    def do(self, data: T) -> Any: ...
