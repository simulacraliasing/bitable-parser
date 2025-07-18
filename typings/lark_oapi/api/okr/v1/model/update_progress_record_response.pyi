from .update_progress_record_response_body import UpdateProgressRecordResponseBody as UpdateProgressRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateProgressRecordResponse(BaseResponse):
    data: UpdateProgressRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
