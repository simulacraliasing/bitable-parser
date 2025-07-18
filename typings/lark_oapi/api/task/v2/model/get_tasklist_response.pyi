from .get_tasklist_response_body import GetTasklistResponseBody as GetTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetTasklistResponse(BaseResponse):
    data: GetTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
