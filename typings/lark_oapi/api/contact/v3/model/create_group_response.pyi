from .create_group_response_body import CreateGroupResponseBody as CreateGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateGroupResponse(BaseResponse):
    data: CreateGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
