from .create_offer_response_body import CreateOfferResponseBody as CreateOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateOfferResponse(BaseResponse):
    data: CreateOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
