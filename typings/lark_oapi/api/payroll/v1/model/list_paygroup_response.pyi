from .list_paygroup_response_body import ListPaygroupResponseBody as ListPaygroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPaygroupResponse(BaseResponse):
    data: ListPaygroupResponseBody | None
    def __init__(self, d=None) -> None: ...
