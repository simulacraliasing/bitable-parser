from .list_file_comment_reply_response_body import ListFileCommentReplyResponseBody as ListFileCommentReplyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFileCommentReplyResponse(BaseResponse):
    data: ListFileCommentReplyResponseBody | None
    def __init__(self, d=None) -> None: ...
