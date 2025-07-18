from .delete_managers_chat_managers_response_body import DeleteManagersChatManagersResponseBody as DeleteManagersChatManagersResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteManagersChatManagersResponse(BaseResponse):
    data: DeleteManagersChatManagersResponseBody | None
    def __init__(self, d=None) -> None: ...
