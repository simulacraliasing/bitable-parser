from .update_badge_grant_response_body import UpdateBadgeGrantResponseBody as UpdateBadgeGrantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateBadgeGrantResponse(BaseResponse):
    data: UpdateBadgeGrantResponseBody | None
    def __init__(self, d=None) -> None: ...
