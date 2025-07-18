from .update_badge_response_body import UpdateBadgeResponseBody as UpdateBadgeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateBadgeResponse(BaseResponse):
    data: UpdateBadgeResponseBody | None
    def __init__(self, d=None) -> None: ...
