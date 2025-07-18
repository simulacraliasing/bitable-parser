from .list_security_group_response_body import ListSecurityGroupResponseBody as ListSecurityGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSecurityGroupResponse(BaseResponse):
    data: ListSecurityGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
