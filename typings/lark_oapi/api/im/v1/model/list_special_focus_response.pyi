from typing import *
from .list_special_focus_response_body import ListSpecialFocusResponseBody as ListSpecialFocusResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSpecialFocusResponse(BaseResponse):
    data: Optional[ListSpecialFocusResponseBody]
    def __init__(self, d=None) -> None: ...
