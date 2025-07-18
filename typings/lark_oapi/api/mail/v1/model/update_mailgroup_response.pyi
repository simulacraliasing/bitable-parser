from .update_mailgroup_response_body import UpdateMailgroupResponseBody as UpdateMailgroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateMailgroupResponse(BaseResponse):
    data: UpdateMailgroupResponseBody | None
    def __init__(self, d=None) -> None: ...
