from ..model.get_chat_moderation_request import GetChatModerationRequest as GetChatModerationRequest
from ..model.get_chat_moderation_response import GetChatModerationResponse as GetChatModerationResponse
from ..model.update_chat_moderation_request import UpdateChatModerationRequest as UpdateChatModerationRequest
from ..model.update_chat_moderation_response import UpdateChatModerationResponse as UpdateChatModerationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ChatModeration:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetChatModerationRequest, option: RequestOption | None = None) -> GetChatModerationResponse: ...
    async def aget(self, request: GetChatModerationRequest, option: RequestOption | None = None) -> GetChatModerationResponse: ...
    def update(self, request: UpdateChatModerationRequest, option: RequestOption | None = None) -> UpdateChatModerationResponse: ...
    async def aupdate(self, request: UpdateChatModerationRequest, option: RequestOption | None = None) -> UpdateChatModerationResponse: ...
