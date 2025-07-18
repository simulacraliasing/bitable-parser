from .batch_create_app_table_response_body import BatchCreateAppTableResponseBody as BatchCreateAppTableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateAppTableResponse(BaseResponse):
    data: BatchCreateAppTableResponseBody | None
    def __init__(self, d=None) -> None: ...
