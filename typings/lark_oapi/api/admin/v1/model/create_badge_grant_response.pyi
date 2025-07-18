from .create_badge_grant_response_body import CreateBadgeGrantResponseBody as CreateBadgeGrantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateBadgeGrantResponse(BaseResponse):
    data: CreateBadgeGrantResponseBody | None
    def __init__(self, d=None) -> None: ...
