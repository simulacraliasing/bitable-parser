from .update_external_offer_response_body import UpdateExternalOfferResponseBody as UpdateExternalOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateExternalOfferResponse(BaseResponse):
    data: UpdateExternalOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
