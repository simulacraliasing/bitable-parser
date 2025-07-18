from .recognize_food_produce_license_response_body import RecognizeFoodProduceLicenseResponseBody as RecognizeFoodProduceLicenseResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeFoodProduceLicenseResponse(BaseResponse):
    data: RecognizeFoodProduceLicenseResponseBody | None
    def __init__(self, d=None) -> None: ...
