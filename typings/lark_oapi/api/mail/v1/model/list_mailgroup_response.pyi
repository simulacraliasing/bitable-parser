from .list_mailgroup_response_body import ListMailgroupResponseBody as ListMailgroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMailgroupResponse(BaseResponse):
    data: ListMailgroupResponseBody | None
    def __init__(self, d=None) -> None: ...
