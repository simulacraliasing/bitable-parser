from .patch_user_response_body import PatchUserResponseBody as PatchUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchUserResponse(BaseResponse):
    data: PatchUserResponseBody | None
    def __init__(self, d=None) -> None: ...
