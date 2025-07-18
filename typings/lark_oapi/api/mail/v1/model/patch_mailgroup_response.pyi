from .patch_mailgroup_response_body import PatchMailgroupResponseBody as PatchMailgroupResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchMailgroupResponse(BaseResponse):
    data: PatchMailgroupResponseBody | None
    def __init__(self, d=None) -> None: ...
