from ..model.batch_update_url_preview_request import BatchUpdateUrlPreviewRequest as BatchUpdateUrlPreviewRequest
from ..model.batch_update_url_preview_response import BatchUpdateUrlPreviewResponse as BatchUpdateUrlPreviewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class UrlPreview:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def batch_update(self, request: BatchUpdateUrlPreviewRequest, option: RequestOption | None = None) -> BatchUpdateUrlPreviewResponse: ...
    async def abatch_update(self, request: BatchUpdateUrlPreviewRequest, option: RequestOption | None = None) -> BatchUpdateUrlPreviewResponse: ...
