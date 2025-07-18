from .create_user_response_body import CreateUserResponseBody as CreateUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateUserResponse(BaseResponse):
    data: CreateUserResponseBody | None
    def __init__(self, d=None) -> None: ...
