from .create_visitor_response_body import CreateVisitorResponseBody as CreateVisitorResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateVisitorResponse(BaseResponse):
    data: CreateVisitorResponseBody | None
    def __init__(self, d=None) -> None: ...
