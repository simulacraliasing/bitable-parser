from .create_category_response_body import CreateCategoryResponseBody as CreateCategoryResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCategoryResponse(BaseResponse):
    data: CreateCategoryResponseBody | None
    def __init__(self, d=None) -> None: ...
