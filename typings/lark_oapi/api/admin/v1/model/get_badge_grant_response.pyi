from .get_badge_grant_response_body import GetBadgeGrantResponseBody as GetBadgeGrantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetBadgeGrantResponse(BaseResponse):
    data: GetBadgeGrantResponseBody | None
    def __init__(self, d=None) -> None: ...
