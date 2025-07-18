from .list_app_table_view_response_body import ListAppTableViewResponseBody as ListAppTableViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppTableViewResponse(BaseResponse):
    data: ListAppTableViewResponseBody | None
    def __init__(self, d=None) -> None: ...
