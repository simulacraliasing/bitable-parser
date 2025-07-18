from .list_task_reminder_response_body import ListTaskReminderResponseBody as ListTaskReminderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTaskReminderResponse(BaseResponse):
    data: ListTaskReminderResponseBody | None
    def __init__(self, d=None) -> None: ...
