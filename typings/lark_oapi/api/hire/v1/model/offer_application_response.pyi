from .offer_application_response_body import OfferApplicationResponseBody as OfferApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class OfferApplicationResponse(BaseResponse):
    data: OfferApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
