from .list_offer_application_form_response_body import ListOfferApplicationFormResponseBody as ListOfferApplicationFormResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListOfferApplicationFormResponse(BaseResponse):
    data: ListOfferApplicationFormResponseBody | None
    def __init__(self, d=None) -> None: ...
