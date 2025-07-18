from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class TasksTasklistRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    completed: bool | None
    created_from: int | None
    created_to: int | None
    user_id_type: str | None
    tasklist_guid: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> TasksTasklistRequestBuilder: ...

class TasksTasklistRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> TasksTasklistRequestBuilder: ...
    def page_token(self, page_token: str) -> TasksTasklistRequestBuilder: ...
    def completed(self, completed: bool) -> TasksTasklistRequestBuilder: ...
    def created_from(self, created_from: int) -> TasksTasklistRequestBuilder: ...
    def created_to(self, created_to: int) -> TasksTasklistRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> TasksTasklistRequestBuilder: ...
    def tasklist_guid(self, tasklist_guid: str) -> TasksTasklistRequestBuilder: ...
    def build(self) -> TasksTasklistRequest: ...
