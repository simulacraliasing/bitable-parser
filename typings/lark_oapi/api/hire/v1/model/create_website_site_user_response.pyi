from .create_website_site_user_response_body import CreateWebsiteSiteUserResponseBody as CreateWebsiteSiteUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateWebsiteSiteUserResponse(BaseResponse):
    data: CreateWebsiteSiteUserResponseBody | None
    def __init__(self, d=None) -> None: ...
