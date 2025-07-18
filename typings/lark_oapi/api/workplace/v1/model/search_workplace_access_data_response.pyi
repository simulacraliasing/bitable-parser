from .search_workplace_access_data_response_body import SearchWorkplaceAccessDataResponseBody as SearchWorkplaceAccessDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchWorkplaceAccessDataResponse(BaseResponse):
    data: SearchWorkplaceAccessDataResponseBody | None
    def __init__(self, d=None) -> None: ...
