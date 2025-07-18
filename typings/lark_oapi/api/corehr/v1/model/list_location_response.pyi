from .list_location_response_body import ListLocationResponseBody as ListLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListLocationResponse(BaseResponse):
    data: ListLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
