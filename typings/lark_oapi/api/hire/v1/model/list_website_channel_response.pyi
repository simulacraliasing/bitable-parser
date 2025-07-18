from .list_website_channel_response_body import ListWebsiteChannelResponseBody as ListWebsiteChannelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWebsiteChannelResponse(BaseResponse):
    data: ListWebsiteChannelResponseBody | None
    def __init__(self, d=None) -> None: ...
