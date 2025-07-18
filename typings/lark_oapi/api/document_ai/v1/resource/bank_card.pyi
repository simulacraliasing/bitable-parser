from ..model.recognize_bank_card_request import RecognizeBankCardRequest as RecognizeBankCardRequest
from ..model.recognize_bank_card_response import RecognizeBankCardResponse as RecognizeBankCardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class BankCard:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeBankCardRequest, option: RequestOption | None = None) -> RecognizeBankCardResponse: ...
    async def arecognize(self, request: RecognizeBankCardRequest, option: RequestOption | None = None) -> RecognizeBankCardResponse: ...
