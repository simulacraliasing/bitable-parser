from .delete_app_feed_card_batch_response_body import DeleteAppFeedCardBatchResponseBody as DeleteAppFeedCardBatchResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteAppFeedCardBatchResponse(BaseResponse):
    data: DeleteAppFeedCardBatchResponseBody | None
    def __init__(self, d=None) -> None: ...
