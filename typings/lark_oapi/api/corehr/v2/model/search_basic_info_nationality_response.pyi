from .search_basic_info_nationality_response_body import SearchBasicInfoNationalityResponseBody as SearchBasicInfoNationalityResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoNationalityResponse(BaseResponse):
    data: SearchBasicInfoNationalityResponseBody | None
    def __init__(self, d=None) -> None: ...
