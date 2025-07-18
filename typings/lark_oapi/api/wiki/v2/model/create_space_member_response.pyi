from .create_space_member_response_body import CreateSpaceMemberResponseBody as CreateSpaceMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpaceMemberResponse(BaseResponse):
    data: CreateSpaceMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
