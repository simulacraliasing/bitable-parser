from .list_termination_reason_response_body import ListTerminationReasonResponseBody as ListTerminationReasonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListTerminationReasonResponse(BaseResponse):
    data: ListTerminationReasonResponseBody | None
    def __init__(self, d=None) -> None: ...
