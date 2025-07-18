from .delete_tabs_chat_tab_response_body import DeleteTabsChatTabResponseBody as DeleteTabsChatTabResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteTabsChatTabResponse(BaseResponse):
    data: DeleteTabsChatTabResponseBody | None
    def __init__(self, d=None) -> None: ...
