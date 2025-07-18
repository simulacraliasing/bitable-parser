from .get_user_response_body import GetUserResponseBody as GetUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetUserResponse(BaseResponse):
    data: GetUserResponseBody | None
    def __init__(self, d=None) -> None: ...
