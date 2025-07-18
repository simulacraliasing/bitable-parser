from .create_user_mailbox_folder_response_body import CreateUserMailboxFolderResponseBody as CreateUserMailboxFolderResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserMailboxFolderResponse(BaseResponse):
    data: CreateUserMailboxFolderResponseBody | None
    def __init__(self, d=None) -> None: ...
