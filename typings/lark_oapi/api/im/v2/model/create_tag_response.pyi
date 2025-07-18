from .create_tag_response_body import CreateTagResponseBody as CreateTagResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateTagResponse(BaseResponse):
    data: CreateTagResponseBody | None
    def __init__(self, d=None) -> None: ...
