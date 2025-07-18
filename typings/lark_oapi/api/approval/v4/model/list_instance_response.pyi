from .list_instance_response_body import ListInstanceResponseBody as ListInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInstanceResponse(BaseResponse):
    data: ListInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
