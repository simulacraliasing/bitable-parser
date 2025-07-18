from .get_progress_record_response_body import GetProgressRecordResponseBody as GetProgressRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetProgressRecordResponse(BaseResponse):
    data: GetProgressRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
