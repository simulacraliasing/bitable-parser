from .get_offer_application_form_response_body import GetOfferApplicationFormResponseBody as GetOfferApplicationFormResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetOfferApplicationFormResponse(BaseResponse):
    data: GetOfferApplicationFormResponseBody | None
    def __init__(self, d=None) -> None: ...
