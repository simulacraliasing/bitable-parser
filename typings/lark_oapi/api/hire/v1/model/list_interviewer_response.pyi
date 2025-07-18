from .list_interviewer_response_body import ListInterviewerResponseBody as ListInterviewerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewerResponse(BaseResponse):
    data: ListInterviewerResponseBody | None
    def __init__(self, d=None) -> None: ...
