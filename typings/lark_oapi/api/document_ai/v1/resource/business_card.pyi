from ..model.recognize_business_card_request import RecognizeBusinessCardRequest as RecognizeBusinessCardRequest
from ..model.recognize_business_card_response import RecognizeBusinessCardResponse as RecognizeBusinessCardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class BusinessCard:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeBusinessCardRequest, option: RequestOption | None = None) -> RecognizeBusinessCardResponse: ...
    async def arecognize(self, request: RecognizeBusinessCardRequest, option: RequestOption | None = None) -> RecognizeBusinessCardResponse: ...
