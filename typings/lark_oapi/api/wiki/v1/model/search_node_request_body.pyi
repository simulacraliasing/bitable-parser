from lark_oapi.core.construct import init as init

class SearchNodeRequestBody:
    query: str | None
    space_id: str | None
    node_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SearchNodeRequestBodyBuilder: ...

class SearchNodeRequestBodyBuilder:
    def __init__(self) -> None: ...
    def query(self, query: str) -> SearchNodeRequestBodyBuilder: ...
    def space_id(self, space_id: str) -> SearchNodeRequestBodyBuilder: ...
    def node_id(self, node_id: str) -> SearchNodeRequestBodyBuilder: ...
    def build(self) -> SearchNodeRequestBody: ...
