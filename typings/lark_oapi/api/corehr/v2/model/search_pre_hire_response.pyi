from .search_pre_hire_response_body import SearchPreHireResponseBody as SearchPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchPreHireResponse(BaseResponse):
    data: SearchPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
