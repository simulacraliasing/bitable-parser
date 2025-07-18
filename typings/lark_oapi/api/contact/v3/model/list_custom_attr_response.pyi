from .list_custom_attr_response_body import ListCustomAttrResponseBody as ListCustomAttrResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCustomAttrResponse(BaseResponse):
    data: ListCustomAttrResponseBody | None
    def __init__(self, d=None) -> None: ...
