from .list_interview_round_type_response_body import ListInterviewRoundTypeResponseBody as ListInterviewRoundTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewRoundTypeResponse(BaseResponse):
    data: ListInterviewRoundTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
