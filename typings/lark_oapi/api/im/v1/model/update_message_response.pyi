from .update_message_response_body import UpdateMessageResponseBody as UpdateMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateMessageResponse(BaseResponse):
    data: UpdateMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
