from .list_interview_response_body import ListInterviewResponseBody as ListInterviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewResponse(BaseResponse):
    data: ListInterviewResponseBody | None
    def __init__(self, d=None) -> None: ...
