from .list_user_okr_response_body import ListUserOkrResponseBody as ListUserOkrResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUserOkrResponse(BaseResponse):
    data: ListUserOkrResponseBody | None
    def __init__(self, d=None) -> None: ...
