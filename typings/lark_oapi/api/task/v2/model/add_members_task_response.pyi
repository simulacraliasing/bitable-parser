from .add_members_task_response_body import AddMembersTaskResponseBody as AddMembersTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddMembersTaskResponse(BaseResponse):
    data: AddMembersTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
