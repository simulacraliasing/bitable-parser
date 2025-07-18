from .create_app_table_record_response_body import CreateAppTableRecordResponseBody as CreateAppTableRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppTableRecordResponse(BaseResponse):
    data: CreateAppTableRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
