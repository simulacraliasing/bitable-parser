from .list_acct_item_response_body import ListAcctItemResponseBody as ListAcctItemResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAcctItemResponse(BaseResponse):
    data: ListAcctItemResponseBody | None
    def __init__(self, d=None) -> None: ...
