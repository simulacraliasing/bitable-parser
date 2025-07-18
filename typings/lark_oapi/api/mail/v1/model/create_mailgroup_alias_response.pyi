from .create_mailgroup_alias_response_body import CreateMailgroupAliasResponseBody as CreateMailgroupAliasResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMailgroupAliasResponse(BaseResponse):
    data: CreateMailgroupAliasResponseBody | None
    def __init__(self, d=None) -> None: ...
