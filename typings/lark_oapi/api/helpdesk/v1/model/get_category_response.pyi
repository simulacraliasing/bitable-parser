from .get_category_response_body import GetCategoryResponseBody as GetCategoryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCategoryResponse(BaseResponse):
    data: GetCategoryResponseBody | None
    def __init__(self, d=None) -> None: ...
