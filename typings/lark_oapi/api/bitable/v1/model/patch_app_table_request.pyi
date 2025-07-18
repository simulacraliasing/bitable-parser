from .patch_app_table_request_body import PatchAppTableRequestBody as PatchAppTableRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchAppTableRequest(BaseRequest):
    app_token: str | None
    table_id: str | None
    request_body: PatchAppTableRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchAppTableRequestBuilder: ...

class PatchAppTableRequestBuilder:
    def __init__(self) -> None: ...
    def app_token(self, app_token: str) -> PatchAppTableRequestBuilder: ...
    def table_id(self, table_id: str) -> PatchAppTableRequestBuilder: ...
    def request_body(self, request_body: PatchAppTableRequestBody) -> PatchAppTableRequestBuilder: ...
    def build(self) -> PatchAppTableRequest: ...
