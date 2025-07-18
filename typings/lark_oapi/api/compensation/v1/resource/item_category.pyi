from ..model.list_item_category_request import ListItemCategoryRequest as ListItemCategoryRequest
from ..model.list_item_category_response import ListItemCategoryResponse as ListItemCategoryResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ItemCategory:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListItemCategoryRequest, option: RequestOption | None = None) -> ListItemCategoryResponse: ...
    async def alist(self, request: ListItemCategoryRequest, option: RequestOption | None = None) -> ListItemCategoryResponse: ...
