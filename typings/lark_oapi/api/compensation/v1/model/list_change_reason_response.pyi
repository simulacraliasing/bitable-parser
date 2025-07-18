from .list_change_reason_response_body import ListChangeReasonResponseBody as ListChangeReasonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListChangeReasonResponse(BaseResponse):
    data: ListChangeReasonResponseBody | None
    def __init__(self, d=None) -> None: ...
