from .list_exam_marking_task_response_body import ListExamMarkingTaskResponseBody as ListExamMarkingTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListExamMarkingTaskResponse(BaseResponse):
    data: ListExamMarkingTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
