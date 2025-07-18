from .list_evaluation_task_response_body import ListEvaluationTaskResponseBody as ListEvaluationTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListEvaluationTaskResponse(BaseResponse):
    data: ListEvaluationTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
