from .query_reviewee_response_body import QueryRevieweeResponseBody as QueryRevieweeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryRevieweeResponse(BaseResponse):
    data: QueryRevieweeResponseBody | None
    def __init__(self, d=None) -> None: ...
