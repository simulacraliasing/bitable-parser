from .list_group_response_body import ListGroupResponseBody as ListGroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListGroupResponse(BaseResponse):
    data: ListGroupResponseBody | None
    def __init__(self, d=None) -> None: ...
