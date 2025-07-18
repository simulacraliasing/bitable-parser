from .update_tabs_chat_tab_response_body import UpdateTabsChatTabResponseBody as UpdateTabsChatTabResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateTabsChatTabResponse(BaseResponse):
    data: UpdateTabsChatTabResponseBody | None
    def __init__(self, d=None) -> None: ...
