from .delete_chat_members_response_body import DeleteChatMembersResponseBody as DeleteChatMembersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteChatMembersResponse(BaseResponse):
    data: DeleteChatMembersResponseBody | None
    def __init__(self, d=None) -> None: ...
