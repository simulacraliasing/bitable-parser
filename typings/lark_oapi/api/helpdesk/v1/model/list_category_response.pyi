from .list_category_response_body import ListCategoryResponseBody as ListCategoryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCategoryResponse(BaseResponse):
    data: ListCategoryResponseBody | None
    def __init__(self, d=None) -> None: ...
