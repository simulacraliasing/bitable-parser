from .query_review_response_body import QueryReviewResponseBody as QueryReviewResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryReviewResponse(BaseResponse):
    data: QueryReviewResponseBody | None
    def __init__(self, d=None) -> None: ...
