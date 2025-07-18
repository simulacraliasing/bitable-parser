from .create_external_offer_response_body import CreateExternalOfferResponseBody as CreateExternalOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalOfferResponse(BaseResponse):
    data: CreateExternalOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
