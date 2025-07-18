from .create_tasklist_response_body import CreateTasklistResponseBody as CreateTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTasklistResponse(BaseResponse):
    data: CreateTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
