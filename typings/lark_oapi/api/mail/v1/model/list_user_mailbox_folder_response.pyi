from .list_user_mailbox_folder_response_body import ListUserMailboxFolderResponseBody as ListUserMailboxFolderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserMailboxFolderResponse(BaseResponse):
    data: ListUserMailboxFolderResponseBody | None
    def __init__(self, d=None) -> None: ...
