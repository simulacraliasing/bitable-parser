from .create_system_status_response_body import CreateSystemStatusResponseBody as CreateSystemStatusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSystemStatusResponse(BaseResponse):
    data: CreateSystemStatusResponseBody | None
    def __init__(self, d=None) -> None: ...
