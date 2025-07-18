from .download_url_user_mailbox_message_attachment_response_body import DownloadUrlUserMailboxMessageAttachmentResponseBody as DownloadUrlUserMailboxMessageAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DownloadUrlUserMailboxMessageAttachmentResponse(BaseResponse):
    data: DownloadUrlUserMailboxMessageAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
