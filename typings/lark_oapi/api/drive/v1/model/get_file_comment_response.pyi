from .get_file_comment_response_body import GetFileCommentResponseBody as GetFileCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetFileCommentResponse(BaseResponse):
    data: GetFileCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
