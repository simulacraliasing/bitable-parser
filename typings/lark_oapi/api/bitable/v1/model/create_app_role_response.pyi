from .create_app_role_response_body import CreateAppRoleResponseBody as CreateAppRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppRoleResponse(BaseResponse):
    data: CreateAppRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
