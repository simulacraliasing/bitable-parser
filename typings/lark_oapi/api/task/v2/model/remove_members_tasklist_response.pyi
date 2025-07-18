from .remove_members_tasklist_response_body import RemoveMembersTasklistResponseBody as RemoveMembersTasklistResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveMembersTasklistResponse(BaseResponse):
    data: RemoveMembersTasklistResponseBody | None
    def __init__(self, d=None) -> None: ...
