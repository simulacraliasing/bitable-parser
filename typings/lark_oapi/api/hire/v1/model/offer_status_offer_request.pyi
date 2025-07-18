from .offer_status_offer_request_body import OfferStatusOfferRequestBody as OfferStatusOfferRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class OfferStatusOfferRequest(BaseRequest):
    offer_id: str | None
    request_body: OfferStatusOfferRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> OfferStatusOfferRequestBuilder: ...

class OfferStatusOfferRequestBuilder:
    def __init__(self) -> None: ...
    def offer_id(self, offer_id: str) -> OfferStatusOfferRequestBuilder: ...
    def request_body(self, request_body: OfferStatusOfferRequestBody) -> OfferStatusOfferRequestBuilder: ...
    def build(self) -> OfferStatusOfferRequest: ...
