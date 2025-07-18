from .list_item_response_body import ListItemResponseBody as ListItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListItemResponse(BaseResponse):
    data: ListItemResponseBody | None
    def __init__(self, d=None) -> None: ...
