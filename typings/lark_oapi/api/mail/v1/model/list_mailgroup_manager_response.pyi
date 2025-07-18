from .list_mailgroup_manager_response_body import ListMailgroupManagerResponseBody as ListMailgroupManagerResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMailgroupManagerResponse(BaseResponse):
    data: ListMailgroupManagerResponseBody | None
    def __init__(self, d=None) -> None: ...
