from .create_timeoff_event_response_body import CreateTimeoffEventResponseBody as CreateTimeoffEventResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTimeoffEventResponse(BaseResponse):
    data: CreateTimeoffEventResponseBody | None
    def __init__(self, d=None) -> None: ...
