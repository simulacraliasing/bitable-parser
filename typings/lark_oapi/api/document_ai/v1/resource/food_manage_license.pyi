from ..model.recognize_food_manage_license_request import RecognizeFoodManageLicenseRequest as RecognizeFoodManageLicenseRequest
from ..model.recognize_food_manage_license_response import RecognizeFoodManageLicenseResponse as RecognizeFoodManageLicenseResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class FoodManageLicense:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeFoodManageLicenseRequest, option: RequestOption | None = None) -> RecognizeFoodManageLicenseResponse: ...
    async def arecognize(self, request: RecognizeFoodManageLicenseRequest, option: RequestOption | None = None) -> RecognizeFoodManageLicenseResponse: ...
