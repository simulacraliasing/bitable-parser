from .list_data_openapi_log_response_body import ListDataOpenapiLogResponseBody as ListDataOpenapiLogResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListDataOpenapiLogResponse(BaseResponse):
    data: ListDataOpenapiLogResponseBody | None
    def __init__(self, d=None) -> None: ...
