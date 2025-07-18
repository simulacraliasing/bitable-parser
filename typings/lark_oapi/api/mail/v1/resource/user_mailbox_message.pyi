from ..model.get_by_card_user_mailbox_message_request import GetByCardUserMailboxMessageRequest as GetByCardUserMailboxMessageRequest
from ..model.get_by_card_user_mailbox_message_response import GetByCardUserMailboxMessageResponse as GetByCardUserMailboxMessageResponse
from ..model.get_user_mailbox_message_request import GetUserMailboxMessageRequest as GetUserMailboxMessageRequest
from ..model.get_user_mailbox_message_response import GetUserMailboxMessageResponse as GetUserMailboxMessageResponse
from ..model.list_user_mailbox_message_request import ListUserMailboxMessageRequest as ListUserMailboxMessageRequest
from ..model.list_user_mailbox_message_response import ListUserMailboxMessageResponse as ListUserMailboxMessageResponse
from ..model.send_user_mailbox_message_request import SendUserMailboxMessageRequest as SendUserMailboxMessageRequest
from ..model.send_user_mailbox_message_response import SendUserMailboxMessageResponse as SendUserMailboxMessageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UserMailboxMessage:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetUserMailboxMessageRequest, option: RequestOption | None = None) -> GetUserMailboxMessageResponse: ...
    async def aget(self, request: GetUserMailboxMessageRequest, option: RequestOption | None = None) -> GetUserMailboxMessageResponse: ...
    def get_by_card(self, request: GetByCardUserMailboxMessageRequest, option: RequestOption | None = None) -> GetByCardUserMailboxMessageResponse: ...
    async def aget_by_card(self, request: GetByCardUserMailboxMessageRequest, option: RequestOption | None = None) -> GetByCardUserMailboxMessageResponse: ...
    def list(self, request: ListUserMailboxMessageRequest, option: RequestOption | None = None) -> ListUserMailboxMessageResponse: ...
    async def alist(self, request: ListUserMailboxMessageRequest, option: RequestOption | None = None) -> ListUserMailboxMessageResponse: ...
    def send(self, request: SendUserMailboxMessageRequest, option: RequestOption | None = None) -> SendUserMailboxMessageResponse: ...
    async def asend(self, request: SendUserMailboxMessageRequest, option: RequestOption | None = None) -> SendUserMailboxMessageResponse: ...
