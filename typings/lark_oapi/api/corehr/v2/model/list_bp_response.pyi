from .list_bp_response_body import ListBpResponseBody as ListBpResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListBpResponse(BaseResponse):
    data: ListBpResponseBody | None
    def __init__(self, d=None) -> None: ...
