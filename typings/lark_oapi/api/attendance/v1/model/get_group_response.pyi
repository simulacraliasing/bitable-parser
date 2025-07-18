from .get_group_response_body import GetGroupResponseBody as GetGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetGroupResponse(BaseResponse):
    data: GetGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
