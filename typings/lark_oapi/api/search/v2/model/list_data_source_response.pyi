from .list_data_source_response_body import ListDataSourceResponseBody as ListDataSourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDataSourceResponse(BaseResponse):
    data: ListDataSourceResponseBody | None
    def __init__(self, d=None) -> None: ...
