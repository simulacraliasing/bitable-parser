from .repo import Repo as Repo
from lark_oapi.core.construct import init as init

class ListRepoResponseBody:
    items: list[Repo] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListRepoResponseBodyBuilder: ...

class ListRepoResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[Repo]) -> ListRepoResponseBodyBuilder: ...
    def build(self) -> ListRepoResponseBody: ...
