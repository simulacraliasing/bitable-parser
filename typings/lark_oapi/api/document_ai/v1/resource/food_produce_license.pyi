from ..model.recognize_food_produce_license_request import RecognizeFoodProduceLicenseRequest as RecognizeFoodProduceLicenseRequest
from ..model.recognize_food_produce_license_response import RecognizeFoodProduceLicenseResponse as RecognizeFoodProduceLicenseResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class FoodProduceLicense:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeFoodProduceLicenseRequest, option: RequestOption | None = None) -> RecognizeFoodProduceLicenseResponse: ...
    async def arecognize(self, request: RecognizeFoodProduceLicenseRequest, option: RequestOption | None = None) -> RecognizeFoodProduceLicenseResponse: ...
