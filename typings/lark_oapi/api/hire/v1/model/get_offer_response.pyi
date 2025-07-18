from .get_offer_response_body import GetOfferResponseBody as GetOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetOfferResponse(BaseResponse):
    data: GetOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
