from ..model.list_location_request import ListLocationRequest as ListLocationRequest
from ..model.list_location_response import ListLocationResponse as ListLocationResponse
from ..model.query_location_request import QueryLocationRequest as QueryLocationRequest
from ..model.query_location_response import QueryLocationResponse as QueryLocationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Location:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def list(self, request: ListLocationRequest, option: RequestOption | None = None) -> ListLocationResponse: ...
    async def alist(self, request: ListLocationRequest, option: RequestOption | None = None) -> ListLocationResponse: ...
    def query(self, request: QueryLocationRequest, option: RequestOption | None = None) -> QueryLocationResponse: ...
    async def aquery(self, request: QueryLocationRequest, option: RequestOption | None = None) -> QueryLocationResponse: ...
