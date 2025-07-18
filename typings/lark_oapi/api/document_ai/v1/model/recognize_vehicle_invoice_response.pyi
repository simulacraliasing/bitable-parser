from .recognize_vehicle_invoice_response_body import RecognizeVehicleInvoiceResponseBody as RecognizeVehicleInvoiceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeVehicleInvoiceResponse(BaseResponse):
    data: RecognizeVehicleInvoiceResponseBody | None
    def __init__(self, d=None) -> None: ...
