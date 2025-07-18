from .update_task_comment_response_body import UpdateTaskCommentResponseBody as UpdateTaskCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateTaskCommentResponse(BaseResponse):
    data: UpdateTaskCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
