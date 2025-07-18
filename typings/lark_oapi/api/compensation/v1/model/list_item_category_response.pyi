from .list_item_category_response_body import ListItemCategoryResponseBody as ListItemCategoryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListItemCategoryResponse(BaseResponse):
    data: ListItemCategoryResponseBody | None
    def __init__(self, d=None) -> None: ...
