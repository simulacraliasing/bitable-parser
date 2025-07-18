from .patch_tag_request_body import PatchTagRequestBody as PatchTagRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchTagRequest(BaseRequest):
    tag_id: str | None
    request_body: PatchTagRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchTagRequestBuilder: ...

class PatchTagRequestBuilder:
    def __init__(self) -> None: ...
    def tag_id(self, tag_id: str) -> PatchTagRequestBuilder: ...
    def request_body(self, request_body: PatchTagRequestBody) -> PatchTagRequestBuilder: ...
    def build(self) -> PatchTagRequest: ...
