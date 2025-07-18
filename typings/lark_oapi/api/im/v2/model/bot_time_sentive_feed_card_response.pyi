from .bot_time_sentive_feed_card_response_body import BotTimeSentiveFeedCardResponseBody as BotTimeSentiveFeedCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BotTimeSentiveFeedCardResponse(BaseResponse):
    data: BotTimeSentiveFeedCardResponseBody | None
    def __init__(self, d=None) -> None: ...
