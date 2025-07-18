from .list_application_interview_response_body import ListApplicationInterviewResponseBody as ListApplicationInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListApplicationInterviewResponse(BaseResponse):
    data: ListApplicationInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
