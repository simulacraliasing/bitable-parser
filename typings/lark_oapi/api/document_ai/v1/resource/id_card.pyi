from ..model.recognize_id_card_request import RecognizeIdCardRequest as RecognizeIdCardRequest
from ..model.recognize_id_card_response import RecognizeIdCardResponse as RecognizeIdCardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class IdCard:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeIdCardRequest, option: RequestOption | None = None) -> RecognizeIdCardResponse: ...
    async def arecognize(self, request: RecognizeIdCardRequest, option: RequestOption | None = None) -> RecognizeIdCardResponse: ...
