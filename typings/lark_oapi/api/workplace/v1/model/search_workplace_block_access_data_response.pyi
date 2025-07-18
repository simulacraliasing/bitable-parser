from .search_workplace_block_access_data_response_body import SearchWorkplaceBlockAccessDataResponseBody as SearchWorkplaceBlockAccessDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchWorkplaceBlockAccessDataResponse(BaseResponse):
    data: SearchWorkplaceBlockAccessDataResponseBody | None
    def __init__(self, d=None) -> None: ...
