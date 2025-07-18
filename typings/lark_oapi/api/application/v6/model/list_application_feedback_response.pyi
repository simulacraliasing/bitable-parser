from .list_application_feedback_response_body import ListApplicationFeedbackResponseBody as ListApplicationFeedbackResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListApplicationFeedbackResponse(BaseResponse):
    data: ListApplicationFeedbackResponseBody | None
    def __init__(self, d=None) -> None: ...
