from .update_offer_response_body import UpdateOfferResponseBody as UpdateOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateOfferResponse(BaseResponse):
    data: UpdateOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
