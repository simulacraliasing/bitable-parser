from .create_app_feed_card_response_body import CreateAppFeedCardResponseBody as CreateAppFeedCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppFeedCardResponse(BaseResponse):
    data: CreateAppFeedCardResponseBody | None
    def __init__(self, d=None) -> None: ...
