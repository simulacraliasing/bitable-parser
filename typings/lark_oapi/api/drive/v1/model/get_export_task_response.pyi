from .get_export_task_response_body import GetExportTaskResponseBody as GetExportTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetExportTaskResponse(BaseResponse):
    data: GetExportTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
