from .intern_offer_status_offer_response_body import InternOfferStatusOfferResponseBody as InternOfferStatusOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class InternOfferStatusOfferResponse(BaseResponse):
    data: InternOfferStatusOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
