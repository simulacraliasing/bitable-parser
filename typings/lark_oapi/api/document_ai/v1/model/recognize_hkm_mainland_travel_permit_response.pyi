from .recognize_hkm_mainland_travel_permit_response_body import RecognizeHkmMainlandTravelPermitResponseBody as RecognizeHkmMainlandTravelPermitResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeHkmMainlandTravelPermitResponse(BaseResponse):
    data: RecognizeHkmMainlandTravelPermitResponseBody | None
    def __init__(self, d=None) -> None: ...
