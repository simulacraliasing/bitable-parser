from .patch_feed_card_response_body import PatchFeedCardResponseBody as PatchFeedCardResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchFeedCardResponse(BaseResponse):
    data: PatchFeedCardResponseBody | None
    def __init__(self, d=None) -> None: ...
