from .create_functional_role_response_body import CreateFunctionalRoleResponseBody as CreateFunctionalRoleResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFunctionalRoleResponse(BaseResponse):
    data: CreateFunctionalRoleResponseBody | None
    def __init__(self, d=None) -> None: ...
