from .update_website_channel_response_body import UpdateWebsiteChannelResponseBody as UpdateWebsiteChannelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateWebsiteChannelResponse(BaseResponse):
    data: UpdateWebsiteChannelResponseBody | None
    def __init__(self, d=None) -> None: ...
