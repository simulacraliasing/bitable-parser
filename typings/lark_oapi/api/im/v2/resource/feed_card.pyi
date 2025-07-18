from ..model.bot_time_sentive_feed_card_request import BotTimeSentiveFeedCardRequest as BotTimeSentiveFeedCardRequest
from ..model.bot_time_sentive_feed_card_response import BotTimeSentiveFeedCardResponse as BotTimeSentiveFeedCardResponse
from ..model.patch_feed_card_request import PatchFeedCardRequest as PatchFeedCardRequest
from ..model.patch_feed_card_response import PatchFeedCardResponse as PatchFeedCardResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class FeedCard:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def bot_time_sentive(self, request: BotTimeSentiveFeedCardRequest, option: RequestOption | None = None) -> BotTimeSentiveFeedCardResponse: ...
    async def abot_time_sentive(self, request: BotTimeSentiveFeedCardRequest, option: RequestOption | None = None) -> BotTimeSentiveFeedCardResponse: ...
    def patch(self, request: PatchFeedCardRequest, option: RequestOption | None = None) -> PatchFeedCardResponse: ...
    async def apatch(self, request: PatchFeedCardRequest, option: RequestOption | None = None) -> PatchFeedCardResponse: ...
