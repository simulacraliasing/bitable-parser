from .create_import_task_response_body import CreateImportTaskResponseBody as CreateImportTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateImportTaskResponse(BaseResponse):
    data: CreateImportTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
