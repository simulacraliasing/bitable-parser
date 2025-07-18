from .list_space_member_response_body import ListSpaceMemberResponseBody as ListSpaceMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSpaceMemberResponse(BaseResponse):
    data: ListSpaceMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
