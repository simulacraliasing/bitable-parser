from .recognize_taxi_invoice_response_body import RecognizeTaxiInvoiceResponseBody as RecognizeTaxiInvoiceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeTaxiInvoiceResponse(BaseResponse):
    data: RecognizeTaxiInvoiceResponseBody | None
    def __init__(self, d=None) -> None: ...
