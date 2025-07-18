from .patch_person_response_body import PatchPersonResponseBody as PatchPersonResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchPersonResponse(BaseResponse):
    data: PatchPersonResponseBody | None
    def __init__(self, d=None) -> None: ...
