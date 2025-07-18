from .list_interview_feedback_form_response_body import ListInterviewFeedbackFormResponseBody as ListInterviewFeedbackFormResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewFeedbackFormResponse(BaseResponse):
    data: ListInterviewFeedbackFormResponseBody | None
    def __init__(self, d=None) -> None: ...
