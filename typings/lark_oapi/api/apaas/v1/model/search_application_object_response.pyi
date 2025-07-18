from .search_application_object_response_body import SearchApplicationObjectResponseBody as SearchApplicationObjectResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchApplicationObjectResponse(BaseResponse):
    data: SearchApplicationObjectResponseBody | None
    def __init__(self, d=None) -> None: ...
