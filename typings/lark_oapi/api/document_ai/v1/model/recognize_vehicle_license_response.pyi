from .recognize_vehicle_license_response_body import RecognizeVehicleLicenseResponseBody as RecognizeVehicleLicenseResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeVehicleLicenseResponse(BaseResponse):
    data: RecognizeVehicleLicenseResponseBody | None
    def __init__(self, d=None) -> None: ...
