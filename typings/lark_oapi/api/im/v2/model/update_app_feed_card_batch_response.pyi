from .update_app_feed_card_batch_response_body import UpdateAppFeedCardBatchResponseBody as UpdateAppFeedCardBatchResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAppFeedCardBatchResponse(BaseResponse):
    data: UpdateAppFeedCardBatchResponseBody | None
    def __init__(self, d=None) -> None: ...
