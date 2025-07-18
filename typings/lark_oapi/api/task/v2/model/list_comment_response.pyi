from .list_comment_response_body import ListCommentResponseBody as ListCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCommentResponse(BaseResponse):
    data: ListCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
