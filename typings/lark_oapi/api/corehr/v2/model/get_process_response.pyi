from .get_process_response_body import GetProcessResponseBody as GetProcessResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetProcessResponse(BaseResponse):
    data: GetProcessResponseBody | None
    def __init__(self, d=None) -> None: ...
