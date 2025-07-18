from .submit_probation_response_body import SubmitProbationResponseBody as SubmitProbationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SubmitProbationResponse(BaseResponse):
    data: SubmitProbationResponseBody | None
    def __init__(self, d=None) -> None: ...
