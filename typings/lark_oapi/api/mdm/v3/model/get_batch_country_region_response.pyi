from .get_batch_country_region_response_body import GetBatchCountryRegionResponseBody as GetBatchCountryRegionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetBatchCountryRegionResponse(BaseResponse):
    data: GetBatchCountryRegionResponseBody | None
    def __init__(self, d=None) -> None: ...
