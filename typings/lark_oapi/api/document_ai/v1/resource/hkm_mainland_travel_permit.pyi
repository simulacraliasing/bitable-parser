from ..model.recognize_hkm_mainland_travel_permit_request import RecognizeHkmMainlandTravelPermitRequest as RecognizeHkmMainlandTravelPermitRequest
from ..model.recognize_hkm_mainland_travel_permit_response import RecognizeHkmMainlandTravelPermitResponse as RecognizeHkmMainlandTravelPermitResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class HkmMainlandTravelPermit:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeHkmMainlandTravelPermitRequest, option: RequestOption | None = None) -> RecognizeHkmMainlandTravelPermitResponse: ...
    async def arecognize(self, request: RecognizeHkmMainlandTravelPermitRequest, option: RequestOption | None = None) -> RecognizeHkmMainlandTravelPermitResponse: ...
