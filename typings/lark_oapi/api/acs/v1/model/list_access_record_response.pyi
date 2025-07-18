from .list_access_record_response_body import ListAccessRecordResponseBody as ListAccessRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAccessRecordResponse(BaseResponse):
    data: ListAccessRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
