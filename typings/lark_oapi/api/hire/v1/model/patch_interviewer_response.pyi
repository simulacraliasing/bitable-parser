from .patch_interviewer_response_body import PatchInterviewerResponseBody as PatchInterviewerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchInterviewerResponse(BaseResponse):
    data: PatchInterviewerResponseBody | None
    def __init__(self, d=None) -> None: ...
