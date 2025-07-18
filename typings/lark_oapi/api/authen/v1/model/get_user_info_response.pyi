from .get_user_info_response_body import GetUserInfoResponseBody as GetUserInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetUserInfoResponse(BaseResponse):
    data: GetUserInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
