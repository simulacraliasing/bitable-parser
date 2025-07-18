from .recognize_train_invoice_response_body import RecognizeTrainInvoiceResponseBody as RecognizeTrainInvoiceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RecognizeTrainInvoiceResponse(BaseResponse):
    data: RecognizeTrainInvoiceResponseBody | None
    def __init__(self, d=None) -> None: ...
