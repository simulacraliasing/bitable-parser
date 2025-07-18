from .remove_members_task_response_body import RemoveMembersTaskResponseBody as RemoveMembersTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveMembersTaskResponse(BaseResponse):
    data: RemoveMembersTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
