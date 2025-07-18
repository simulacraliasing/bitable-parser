from .create_task_comment_response_body import CreateTaskCommentResponseBody as CreateTaskCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskCommentResponse(BaseResponse):
    data: CreateTaskCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
