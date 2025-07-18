from .intern_offer_status import InternOfferStatus as InternOfferStatus
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class InternOfferStatusOfferRequest(BaseRequest):
    offer_id: str | None
    request_body: InternOfferStatus | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> InternOfferStatusOfferRequestBuilder: ...

class InternOfferStatusOfferRequestBuilder:
    def __init__(self) -> None: ...
    def offer_id(self, offer_id: str) -> InternOfferStatusOfferRequestBuilder: ...
    def request_body(self, request_body: InternOfferStatus) -> InternOfferStatusOfferRequestBuilder: ...
    def build(self) -> InternOfferStatusOfferRequest: ...
