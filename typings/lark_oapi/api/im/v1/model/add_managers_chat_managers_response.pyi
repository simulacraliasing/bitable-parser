from .add_managers_chat_managers_response_body import AddManagersChatManagersResponseBody as AddManagersChatManagersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddManagersChatManagersResponse(BaseResponse):
    data: AddManagersChatManagersResponseBody | None
    def __init__(self, d=None) -> None: ...
