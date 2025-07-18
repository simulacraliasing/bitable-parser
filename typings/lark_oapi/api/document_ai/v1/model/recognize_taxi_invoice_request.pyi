from .recognize_taxi_invoice_request_body import RecognizeTaxiInvoiceRequestBody as RecognizeTaxiInvoiceRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class RecognizeTaxiInvoiceRequest(BaseRequest):
    request_body: RecognizeTaxiInvoiceRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> RecognizeTaxiInvoiceRequestBuilder: ...

class RecognizeTaxiInvoiceRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: RecognizeTaxiInvoiceRequestBody) -> RecognizeTaxiInvoiceRequestBuilder: ...
    def build(self) -> RecognizeTaxiInvoiceRequest: ...
