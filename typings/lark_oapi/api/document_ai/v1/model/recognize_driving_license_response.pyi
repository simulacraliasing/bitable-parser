from .recognize_driving_license_response_body import RecognizeDrivingLicenseResponseBody as RecognizeDrivingLicenseResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeDrivingLicenseResponse(BaseResponse):
    data: RecognizeDrivingLicenseResponseBody | None
    def __init__(self, d=None) -> None: ...
