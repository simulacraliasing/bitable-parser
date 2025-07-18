from .patch_comment_request_body import PatchCommentRequestBody as PatchCommentRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchCommentRequest(BaseRequest):
    user_id_type: str | None
    comment_id: str | None
    request_body: PatchCommentRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchCommentRequestBuilder: ...

class PatchCommentRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> PatchCommentRequestBuilder: ...
    def comment_id(self, comment_id: str) -> PatchCommentRequestBuilder: ...
    def request_body(self, request_body: PatchCommentRequestBody) -> PatchCommentRequestBuilder: ...
    def build(self) -> PatchCommentRequest: ...
