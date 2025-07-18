from .parse_resume_response_body import ParseResumeResponseBody as ParseResumeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ParseResumeResponse(BaseResponse):
    data: ParseResumeResponseBody | None
    def __init__(self, d=None) -> None: ...
