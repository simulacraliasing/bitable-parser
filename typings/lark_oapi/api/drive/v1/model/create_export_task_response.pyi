from .create_export_task_response_body import CreateExportTaskResponseBody as CreateExportTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExportTaskResponse(BaseResponse):
    data: CreateExportTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
