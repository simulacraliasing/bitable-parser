from .chat_group_user_task_response_body import ChatGroupUserTaskResponseBody as ChatGroupUserTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ChatGroupUserTaskResponse(BaseResponse):
    data: ChatGroupUserTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
