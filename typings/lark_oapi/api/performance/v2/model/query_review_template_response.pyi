from .query_review_template_response_body import QueryReviewTemplateResponseBody as QueryReviewTemplateResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryReviewTemplateResponse(BaseResponse):
    data: QueryReviewTemplateResponseBody | None
    def __init__(self, d=None) -> None: ...
