from .list_user_response_body import ListUserResponseBody as ListUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserResponse(BaseResponse):
    data: ListUserResponseBody | None
    def __init__(self, d=None) -> None: ...
