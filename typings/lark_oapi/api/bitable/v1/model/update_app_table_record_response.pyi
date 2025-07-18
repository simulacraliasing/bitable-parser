from .update_app_table_record_response_body import UpdateAppTableRecordResponseBody as UpdateAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAppTableRecordResponse(BaseResponse):
    data: UpdateAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
