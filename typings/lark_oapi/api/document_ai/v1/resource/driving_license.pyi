from ..model.recognize_driving_license_request import RecognizeDrivingLicenseRequest as RecognizeDrivingLicenseRequest
from ..model.recognize_driving_license_response import RecognizeDrivingLicenseResponse as RecognizeDrivingLicenseResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class DrivingLicense:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def recognize(self, request: RecognizeDrivingLicenseRequest, option: RequestOption | None = None) -> RecognizeDrivingLicenseResponse: ...
    async def arecognize(self, request: RecognizeDrivingLicenseRequest, option: RequestOption | None = None) -> RecognizeDrivingLicenseResponse: ...
