from .list_mailgroup_alias_response_body import ListMailgroupAliasResponseBody as ListMailgroupAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListMailgroupAliasResponse(BaseResponse):
    data: ListMailgroupAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
