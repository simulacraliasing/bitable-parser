from .list_app_table_response_body import ListAppTableResponseBody as ListAppTableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppTableResponse(BaseResponse):
    data: ListAppTableResponseBody | None
    def __init__(self, d=None) -> None: ...
