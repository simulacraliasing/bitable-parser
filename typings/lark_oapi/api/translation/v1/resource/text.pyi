from ..model.detect_text_request import DetectTextRequest as DetectTextRequest
from ..model.detect_text_response import DetectTextResponse as DetectTextResponse
from ..model.translate_text_request import TranslateTextRequest as TranslateTextRequest
from ..model.translate_text_response import TranslateTextResponse as TranslateTextResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Text:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def detect(self, request: DetectTextRequest, option: RequestOption | None = None) -> DetectTextResponse: ...
    async def adetect(self, request: DetectTextRequest, option: RequestOption | None = None) -> DetectTextResponse: ...
    def translate(self, request: TranslateTextRequest, option: RequestOption | None = None) -> TranslateTextResponse: ...
    async def atranslate(self, request: TranslateTextRequest, option: RequestOption | None = None) -> TranslateTextResponse: ...
