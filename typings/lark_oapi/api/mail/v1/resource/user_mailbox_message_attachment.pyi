from ..model.download_url_user_mailbox_message_attachment_request import DownloadUrlUserMailboxMessageAttachmentRequest as DownloadUrlUserMailboxMessageAttachmentRequest
from ..model.download_url_user_mailbox_message_attachment_response import DownloadUrlUserMailboxMessageAttachmentResponse as DownloadUrlUserMailboxMessageAttachmentResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserMailboxMessageAttachment:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def download_url(self, request: DownloadUrlUserMailboxMessageAttachmentRequest, option: RequestOption | None = None) -> DownloadUrlUserMailboxMessageAttachmentResponse: ...
    async def adownload_url(self, request: DownloadUrlUserMailboxMessageAttachmentRequest, option: RequestOption | None = None) -> DownloadUrlUserMailboxMessageAttachmentResponse: ...
