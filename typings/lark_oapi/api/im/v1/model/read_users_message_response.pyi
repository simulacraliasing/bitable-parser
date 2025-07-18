from .read_users_message_response_body import ReadUsersMessageResponseBody as ReadUsersMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ReadUsersMessageResponse(BaseResponse):
    data: ReadUsersMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
