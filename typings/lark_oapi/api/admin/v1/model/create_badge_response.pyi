from .create_badge_response_body import CreateBadgeResponseBody as CreateBadgeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateBadgeResponse(BaseResponse):
    data: CreateBadgeResponseBody | None
    def __init__(self, d=None) -> None: ...
