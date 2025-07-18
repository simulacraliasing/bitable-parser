from .revoke_job_change_response_body import RevokeJobChangeResponseBody as RevokeJobChangeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RevokeJobChangeResponse(BaseResponse):
    data: RevokeJobChangeResponseBody | None
    def __init__(self, d=None) -> None: ...
