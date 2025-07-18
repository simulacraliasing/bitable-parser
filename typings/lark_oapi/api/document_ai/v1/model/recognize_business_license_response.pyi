from .recognize_business_license_response_body import RecognizeBusinessLicenseResponseBody as RecognizeBusinessLicenseResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeBusinessLicenseResponse(BaseResponse):
    data: RecognizeBusinessLicenseResponseBody | None
    def __init__(self, d=None) -> None: ...
