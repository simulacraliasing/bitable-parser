from .list_badge_grant_response_body import ListBadgeGrantResponseBody as ListBadgeGrantResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListBadgeGrantResponse(BaseResponse):
    data: ListBadgeGrantResponseBody | None
    def __init__(self, d=None) -> None: ...
