from .list_evaluation_response_body import ListEvaluationResponseBody as ListEvaluationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEvaluationResponse(BaseResponse):
    data: ListEvaluationResponseBody | None
    def __init__(self, d=None) -> None: ...
