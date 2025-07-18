from .get_import_task_response_body import GetImportTaskResponseBody as GetImportTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetImportTaskResponse(BaseResponse):
    data: GetImportTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
