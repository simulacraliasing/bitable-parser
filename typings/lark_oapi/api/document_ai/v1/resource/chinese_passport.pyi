from ..model.recognize_chinese_passport_request import RecognizeChinesePassportRequest as RecognizeChinesePassportRequest
from ..model.recognize_chinese_passport_response import RecognizeChinesePassportResponse as RecognizeChinesePassportResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class ChinesePassport:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeChinesePassportRequest, option: RequestOption | None = None) -> RecognizeChinesePassportResponse: ...
    async def arecognize(self, request: RecognizeChinesePassportRequest, option: RequestOption | None = None) -> RecognizeChinesePassportResponse: ...
