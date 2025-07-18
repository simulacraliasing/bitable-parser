from .update_app_role_response_body import UpdateAppRoleResponseBody as UpdateAppRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAppRoleResponse(BaseResponse):
    data: UpdateAppRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
