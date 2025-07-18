from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListEvaluationTaskRequest(BaseRequest):
    page_size: int | None
    page_token: str | None
    user_id: str | None
    activity_status: int | None
    user_id_type: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListEvaluationTaskRequestBuilder: ...

class ListEvaluationTaskRequestBuilder:
    def __init__(self) -> None: ...
    def page_size(self, page_size: int) -> ListEvaluationTaskRequestBuilder: ...
    def page_token(self, page_token: str) -> ListEvaluationTaskRequestBuilder: ...
    def user_id(self, user_id: str) -> ListEvaluationTaskRequestBuilder: ...
    def activity_status(self, activity_status: int) -> ListEvaluationTaskRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> ListEvaluationTaskRequestBuilder: ...
    def build(self) -> ListEvaluationTaskRequest: ...
