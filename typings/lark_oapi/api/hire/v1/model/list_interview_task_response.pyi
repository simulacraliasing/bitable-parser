from .list_interview_task_response_body import ListInterviewTaskResponseBody as ListInterviewTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInterviewTaskResponse(BaseResponse):
    data: ListInterviewTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
