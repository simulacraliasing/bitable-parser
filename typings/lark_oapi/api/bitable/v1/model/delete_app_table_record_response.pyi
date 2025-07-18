from .delete_app_table_record_response_body import DeleteAppTableRecordResponseBody as DeleteAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteAppTableRecordResponse(BaseResponse):
    data: DeleteAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
