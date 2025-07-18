from lark_oapi.core.construct import init as init

class OpenapiLogDetail:
    path: str | None
    method: str | None
    query_param: str | None
    payload: str | None
    status_code: int | None
    response: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> OpenapiLogDetailBuilder: ...

class OpenapiLogDetailBuilder:
    def __init__(self) -> None: ...
    def path(self, path: str) -> OpenapiLogDetailBuilder: ...
    def method(self, method: str) -> OpenapiLogDetailBuilder: ...
    def query_param(self, query_param: str) -> OpenapiLogDetailBuilder: ...
    def payload(self, payload: str) -> OpenapiLogDetailBuilder: ...
    def status_code(self, status_code: int) -> OpenapiLogDetailBuilder: ...
    def response(self, response: str) -> OpenapiLogDetailBuilder: ...
    def build(self) -> OpenapiLogDetail: ...
