from .list_faq_response_body import ListFaqResponseBody as ListFaqResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListFaqResponse(BaseResponse):
    data: ListFaqResponseBody | None
    def __init__(self, d=None) -> None: ...
