from ..model.delete_top_notice_chat_top_notice_request import DeleteTopNoticeChatTopNoticeRequest as DeleteTopNoticeChatTopNoticeRequest
from ..model.delete_top_notice_chat_top_notice_response import DeleteTopNoticeChatTopNoticeResponse as DeleteTopNoticeChatTopNoticeResponse
from ..model.put_top_notice_chat_top_notice_request import PutTopNoticeChatTopNoticeRequest as PutTopNoticeChatTopNoticeRequest
from ..model.put_top_notice_chat_top_notice_response import PutTopNoticeChatTopNoticeResponse as PutTopNoticeChatTopNoticeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ChatTopNotice:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def delete_top_notice(self, request: DeleteTopNoticeChatTopNoticeRequest, option: RequestOption | None = None) -> DeleteTopNoticeChatTopNoticeResponse: ...
    async def adelete_top_notice(self, request: DeleteTopNoticeChatTopNoticeRequest, option: RequestOption | None = None) -> DeleteTopNoticeChatTopNoticeResponse: ...
    def put_top_notice(self, request: PutTopNoticeChatTopNoticeRequest, option: RequestOption | None = None) -> PutTopNoticeChatTopNoticeResponse: ...
    async def aput_top_notice(self, request: PutTopNoticeChatTopNoticeRequest, option: RequestOption | None = None) -> PutTopNoticeChatTopNoticeResponse: ...
