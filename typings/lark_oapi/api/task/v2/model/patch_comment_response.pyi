from .patch_comment_response_body import PatchCommentResponseBody as PatchCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchCommentResponse(BaseResponse):
    data: PatchCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
