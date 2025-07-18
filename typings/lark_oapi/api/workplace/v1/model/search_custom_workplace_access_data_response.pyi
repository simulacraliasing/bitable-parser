from .search_custom_workplace_access_data_response_body import SearchCustomWorkplaceAccessDataResponseBody as SearchCustomWorkplaceAccessDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchCustomWorkplaceAccessDataResponse(BaseResponse):
    data: SearchCustomWorkplaceAccessDataResponseBody | None
    def __init__(self, d=None) -> None: ...
