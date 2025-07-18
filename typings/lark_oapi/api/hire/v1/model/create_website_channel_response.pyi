from .create_website_channel_response_body import CreateWebsiteChannelResponseBody as CreateWebsiteChannelResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateWebsiteChannelResponse(BaseResponse):
    data: CreateWebsiteChannelResponseBody | None
    def __init__(self, d=None) -> None: ...
