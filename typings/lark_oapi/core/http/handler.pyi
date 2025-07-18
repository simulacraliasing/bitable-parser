import abc
from abc import ABC, abstractmethod
from lark_oapi.core.model import RawRequest as RawRequest, RawResponse as RawResponse

class HttpHandler(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def do(self, req: RawRequest) -> RawResponse: ...
