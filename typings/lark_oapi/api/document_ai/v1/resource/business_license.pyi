from ..model.recognize_business_license_request import RecognizeBusinessLicenseRequest as RecognizeBusinessLicenseRequest
from ..model.recognize_business_license_response import RecognizeBusinessLicenseResponse as RecognizeBusinessLicenseResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class BusinessLicense:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeBusinessLicenseRequest, option: RequestOption | None = None) -> RecognizeBusinessLicenseResponse: ...
    async def arecognize(self, request: RecognizeBusinessLicenseRequest, option: RequestOption | None = None) -> RecognizeBusinessLicenseResponse: ...
