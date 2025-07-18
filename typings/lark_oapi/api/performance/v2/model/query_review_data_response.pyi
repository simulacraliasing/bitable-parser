from .query_review_data_response_body import QueryReviewDataResponseBody as QueryReviewDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryReviewDataResponse(BaseResponse):
    data: QueryReviewDataResponseBody | None
    def __init__(self, d=None) -> None: ...
