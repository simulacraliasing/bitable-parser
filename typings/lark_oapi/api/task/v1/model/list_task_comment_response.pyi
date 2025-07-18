from .list_task_comment_response_body import ListTaskCommentResponseBody as ListTaskCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskCommentResponse(BaseResponse):
    data: ListTaskCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
