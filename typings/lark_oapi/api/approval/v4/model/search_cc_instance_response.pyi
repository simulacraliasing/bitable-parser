from .search_cc_instance_response_body import SearchCcInstanceResponseBody as SearchCcInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchCcInstanceResponse(BaseResponse):
    data: SearchCcInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
