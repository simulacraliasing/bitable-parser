from .get_role_response_body import GetRoleResponseBody as GetRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetRoleResponse(BaseResponse):
    data: GetRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
