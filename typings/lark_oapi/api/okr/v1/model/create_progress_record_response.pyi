from .create_progress_record_response_body import CreateProgressRecordResponseBody as CreateProgressRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateProgressRecordResponse(BaseResponse):
    data: CreateProgressRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
