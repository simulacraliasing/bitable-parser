from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteAppTableViewRequest(BaseRequest):
    app_token: str | None
    table_id: str | None
    view_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteAppTableViewRequestBuilder: ...

class DeleteAppTableViewRequestBuilder:
    def __init__(self) -> None: ...
    def app_token(self, app_token: str) -> DeleteAppTableViewRequestBuilder: ...
    def table_id(self, table_id: str) -> DeleteAppTableViewRequestBuilder: ...
    def view_id(self, view_id: str) -> DeleteAppTableViewRequestBuilder: ...
    def build(self) -> DeleteAppTableViewRequest: ...
