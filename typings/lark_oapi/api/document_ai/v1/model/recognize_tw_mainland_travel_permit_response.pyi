from .recognize_tw_mainland_travel_permit_response_body import RecognizeTwMainlandTravelPermitResponseBody as RecognizeTwMainlandTravelPermitResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeTwMainlandTravelPermitResponse(BaseResponse):
    data: RecognizeTwMainlandTravelPermitResponseBody | None
    def __init__(self, d=None) -> None: ...
