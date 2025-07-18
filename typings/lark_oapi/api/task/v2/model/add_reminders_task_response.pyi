from .add_reminders_task_response_body import AddRemindersTaskResponseBody as AddRemindersTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddRemindersTaskResponse(BaseResponse):
    data: AddRemindersTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
