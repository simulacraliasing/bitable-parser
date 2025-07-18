from .list_unit_response_body import ListUnitResponseBody as ListUnitResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListUnitResponse(BaseResponse):
    data: ListUnitResponseBody | None
    def __init__(self, d=None) -> None: ...
