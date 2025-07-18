from .search_faq_response_body import SearchFaqResponseBody as SearchFaqResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchFaqResponse(BaseResponse):
    data: SearchFaqResponseBody | None
    def __init__(self, d=None) -> None: ...
