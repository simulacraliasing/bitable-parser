from .get_app_table_view_response_body import GetAppTableViewResponseBody as GetAppTableViewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAppTableViewResponse(BaseResponse):
    data: GetAppTableViewResponseBody | None
    def __init__(self, d=None) -> None: ...
