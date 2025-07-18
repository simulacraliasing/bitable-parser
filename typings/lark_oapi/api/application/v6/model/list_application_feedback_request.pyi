from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class ListApplicationFeedbackRequest(BaseRequest):
    from_date: str | None
    to_date: str | None
    feedback_type: int | None
    status: int | None
    user_id_type: str | None
    page_token: int | None
    page_size: int | None
    app_id: str | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> ListApplicationFeedbackRequestBuilder: ...

class ListApplicationFeedbackRequestBuilder:
    def __init__(self) -> None: ...
    def from_date(self, from_date: str) -> ListApplicationFeedbackRequestBuilder: ...
    def to_date(self, to_date: str) -> ListApplicationFeedbackRequestBuilder: ...
    def feedback_type(self, feedback_type: int) -> ListApplicationFeedbackRequestBuilder: ...
    def status(self, status: int) -> ListApplicationFeedbackRequestBuilder: ...
    def user_id_type(self, user_id_type: str) -> ListApplicationFeedbackRequestBuilder: ...
    def page_token(self, page_token: int) -> ListApplicationFeedbackRequestBuilder: ...
    def page_size(self, page_size: int) -> ListApplicationFeedbackRequestBuilder: ...
    def app_id(self, app_id: str) -> ListApplicationFeedbackRequestBuilder: ...
    def build(self) -> ListApplicationFeedbackRequest: ...
