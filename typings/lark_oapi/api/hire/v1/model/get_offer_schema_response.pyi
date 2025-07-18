from .get_offer_schema_response_body import GetOfferSchemaResponseBody as GetOfferSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetOfferSchemaResponse(BaseResponse):
    data: GetOfferSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
