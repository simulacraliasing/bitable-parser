from .create_mailgroup_response_body import CreateMailgroupResponseBody as CreateMailgroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateMailgroupResponse(BaseResponse):
    data: CreateMailgroupResponseBody | None
    def __init__(self, d=None) -> None: ...
