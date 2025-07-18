from .delete_space_member_response_body import DeleteSpaceMemberResponseBody as DeleteSpaceMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteSpaceMemberResponse(BaseResponse):
    data: DeleteSpaceMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
