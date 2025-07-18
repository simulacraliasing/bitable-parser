from .update_user_response_body import UpdateUserResponseBody as UpdateUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateUserResponse(BaseResponse):
    data: UpdateUserResponseBody | None
    def __init__(self, d=None) -> None: ...
