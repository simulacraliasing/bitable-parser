from .list_file_comment_response_body import ListFileCommentResponseBody as ListFileCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileCommentResponse(BaseResponse):
    data: ListFileCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
