from .batch_query_external_offer_response_body import BatchQueryExternalOfferResponseBody as BatchQueryExternalOfferResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryExternalOfferResponse(BaseResponse):
    data: BatchQueryExternalOfferResponseBody | None
    def __init__(self, d=None) -> None: ...
