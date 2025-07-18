from .list_badge_response_body import ListBadgeResponseBody as ListBadgeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListBadgeResponse(BaseResponse):
    data: ListBadgeResponseBody | None
    def __init__(self, d=None) -> None: ...
