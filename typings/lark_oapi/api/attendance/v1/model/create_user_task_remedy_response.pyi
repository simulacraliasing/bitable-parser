from .create_user_task_remedy_response_body import CreateUserTaskRemedyResponseBody as CreateUserTaskRemedyResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserTaskRemedyResponse(BaseResponse):
    data: CreateUserTaskRemedyResponseBody | None
    def __init__(self, d=None) -> None: ...
