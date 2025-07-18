from .list_datasource_response_body import ListDatasourceResponseBody as ListDatasourceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDatasourceResponse(BaseResponse):
    data: ListDatasourceResponseBody | None
    def __init__(self, d=None) -> None: ...
