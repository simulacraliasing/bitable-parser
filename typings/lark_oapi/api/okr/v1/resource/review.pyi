from ..model.query_review_request import QueryReviewRequest as QueryReviewRequest
from ..model.query_review_response import QueryReviewResponse as QueryReviewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Review:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryReviewRequest, option: RequestOption | None = None) -> QueryReviewResponse: ...
    async def aquery(self, request: QueryReviewRequest, option: RequestOption | None = None) -> QueryReviewResponse: ...
