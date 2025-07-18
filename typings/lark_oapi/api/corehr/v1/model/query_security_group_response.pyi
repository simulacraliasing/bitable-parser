from .query_security_group_response_body import QuerySecurityGroupResponseBody as QuerySecurityGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySecurityGroupResponse(BaseResponse):
    data: QuerySecurityGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
