from .query_question_response_body import QueryQuestionResponseBody as QueryQuestionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryQuestionResponse(BaseResponse):
    data: QueryQuestionResponseBody | None
    def __init__(self, d=None) -> None: ...
