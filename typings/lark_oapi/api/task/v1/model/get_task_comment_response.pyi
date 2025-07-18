from .get_task_comment_response_body import GetTaskCommentResponseBody as GetTaskCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTaskCommentResponse(BaseResponse):
    data: GetTaskCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
