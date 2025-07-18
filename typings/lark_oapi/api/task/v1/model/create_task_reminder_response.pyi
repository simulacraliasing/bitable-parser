from .create_task_reminder_response_body import CreateTaskReminderResponseBody as CreateTaskReminderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTaskReminderResponse(BaseResponse):
    data: CreateTaskReminderResponseBody | None
    def __init__(self, d=None) -> None: ...
