from ..model.delete_app_feed_card_batch_request import DeleteAppFeedCardBatchRequest as DeleteAppFeedCardBatchRequest
from ..model.delete_app_feed_card_batch_response import DeleteAppFeedCardBatchResponse as DeleteAppFeedCardBatchResponse
from ..model.update_app_feed_card_batch_request import UpdateAppFeedCardBatchRequest as UpdateAppFeedCardBatchRequest
from ..model.update_app_feed_card_batch_response import UpdateAppFeedCardBatchResponse as UpdateAppFeedCardBatchResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AppFeedCardBatch:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def delete(self, request: DeleteAppFeedCardBatchRequest, option: RequestOption | None = None) -> DeleteAppFeedCardBatchResponse: ...
    async def adelete(self, request: DeleteAppFeedCardBatchRequest, option: RequestOption | None = None) -> DeleteAppFeedCardBatchResponse: ...
    def update(self, request: UpdateAppFeedCardBatchRequest, option: RequestOption | None = None) -> UpdateAppFeedCardBatchResponse: ...
    async def aupdate(self, request: UpdateAppFeedCardBatchRequest, option: RequestOption | None = None) -> UpdateAppFeedCardBatchResponse: ...
