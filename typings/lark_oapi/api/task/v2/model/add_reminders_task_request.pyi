from .add_reminders_task_request_body import AddRemindersTaskRequestBody as AddRemindersTaskRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class AddRemindersTaskRequest(BaseRequest):
    user_id_type: str | None
    task_guid: str | None
    request_body: AddRemindersTaskRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> AddRemindersTaskRequestBuilder: ...

class AddRemindersTaskRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> AddRemindersTaskRequestBuilder: ...
    def task_guid(self, task_guid: str) -> AddRemindersTaskRequestBuilder: ...
    def request_body(self, request_body: AddRemindersTaskRequestBody) -> AddRemindersTaskRequestBuilder: ...
    def build(self) -> AddRemindersTaskRequest: ...
