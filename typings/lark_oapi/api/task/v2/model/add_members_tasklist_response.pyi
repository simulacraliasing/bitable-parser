from .add_members_tasklist_response_body import AddMembersTasklistResponseBody as AddMembersTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddMembersTasklistResponse(BaseResponse):
    data: AddMembersTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
