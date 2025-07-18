from .write_user_group_user_rel_response_body import WriteUserGroupUserRelResponseBody as WriteUserGroupUserRelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class WriteUserGroupUserRelResponse(BaseResponse):
    data: WriteUserGroupUserRelResponseBody | None
    def __init__(self, d=None) -> None: ...
