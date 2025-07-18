from .remove_reminders_task_response_body import RemoveRemindersTaskResponseBody as RemoveRemindersTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveRemindersTaskResponse(BaseResponse):
    data: RemoveRemindersTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
