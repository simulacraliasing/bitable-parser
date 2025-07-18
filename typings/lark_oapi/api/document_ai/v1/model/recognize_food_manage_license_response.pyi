from .recognize_food_manage_license_response_body import RecognizeFoodManageLicenseResponseBody as RecognizeFoodManageLicenseResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeFoodManageLicenseResponse(BaseResponse):
    data: RecognizeFoodManageLicenseResponseBody | None
    def __init__(self, d=None) -> None: ...
