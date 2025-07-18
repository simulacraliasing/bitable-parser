from .get_badge_response_body import GetBadgeResponseBody as GetBadgeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetBadgeResponse(BaseResponse):
    data: GetBadgeResponseBody | None
    def __init__(self, d=None) -> None: ...
