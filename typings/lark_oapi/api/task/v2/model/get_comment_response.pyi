from .get_comment_response_body import GetCommentResponseBody as GetCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCommentResponse(BaseResponse):
    data: GetCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
