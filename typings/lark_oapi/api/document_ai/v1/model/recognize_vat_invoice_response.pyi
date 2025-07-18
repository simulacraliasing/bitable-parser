from .recognize_vat_invoice_response_body import RecognizeVatInvoiceResponseBody as RecognizeVatInvoiceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeVatInvoiceResponse(BaseResponse):
    data: RecognizeVatInvoiceResponseBody | None
    def __init__(self, d=None) -> None: ...
