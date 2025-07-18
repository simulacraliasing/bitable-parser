from .create_message_response_body import CreateMessageResponseBody as CreateMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMessageResponse(BaseResponse):
    data: CreateMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
