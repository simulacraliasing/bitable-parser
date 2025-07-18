from .list_website_response_body import ListWebsiteResponseBody as ListWebsiteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWebsiteResponse(BaseResponse):
    data: ListWebsiteResponseBody | None
    def __init__(self, d=None) -> None: ...
