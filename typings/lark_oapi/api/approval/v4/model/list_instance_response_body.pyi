from lark_oapi.core.construct import init as init

class ListInstanceResponseBody:
    instance_code_list: list[str] | None
    page_token: str | None
    has_more: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListInstanceResponseBodyBuilder: ...

class ListInstanceResponseBodyBuilder:
    def __init__(self) -> None: ...
    def instance_code_list(self, instance_code_list: list[str]) -> ListInstanceResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListInstanceResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListInstanceResponseBodyBuilder: ...
    def build(self) -> ListInstanceResponseBody: ...
