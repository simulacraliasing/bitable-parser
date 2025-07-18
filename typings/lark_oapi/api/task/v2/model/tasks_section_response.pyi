from .tasks_section_response_body import TasksSectionResponseBody as TasksSectionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TasksSectionResponse(BaseResponse):
    data: TasksSectionResponseBody | None
    def __init__(self, d=None) -> None: ...
