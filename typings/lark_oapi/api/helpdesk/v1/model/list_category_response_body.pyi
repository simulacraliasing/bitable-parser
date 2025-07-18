from .category import Category as Category
from lark_oapi.core.construct import init as init

class ListCategoryResponseBody:
    categories: list[Category] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListCategoryResponseBodyBuilder: ...

class ListCategoryResponseBodyBuilder:
    def __init__(self) -> None: ...
    def categories(self, categories: list[Category]) -> ListCategoryResponseBodyBuilder: ...
    def build(self) -> ListCategoryResponseBody: ...
