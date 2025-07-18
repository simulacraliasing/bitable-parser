from lark_oapi.core.construct import init as init

class SearchEnumRequestBody:
    enum_apiname_lists: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchEnumRequestBodyBuilder: ...

class SearchEnumRequestBodyBuilder:
    def __init__(self) -> None: ...
    def enum_apiname_lists(self, enum_apiname_lists: list[str]) -> SearchEnumRequestBodyBuilder: ...
    def build(self) -> SearchEnumRequestBody: ...
