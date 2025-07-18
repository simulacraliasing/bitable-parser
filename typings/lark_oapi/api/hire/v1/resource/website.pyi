from ..model.list_website_request import ListWebsiteRequest as ListWebsiteRequest
from ..model.list_website_response import ListWebsiteResponse as ListWebsiteResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Website:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListWebsiteRequest, option: RequestOption | None = None) -> ListWebsiteResponse: ...
    async def alist(self, request: ListWebsiteRequest, option: RequestOption | None = None) -> ListWebsiteResponse: ...
