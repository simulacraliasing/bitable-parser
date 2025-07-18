from ..model.oql_query_application_object_request import OqlQueryApplicationObjectRequest as OqlQueryApplicationObjectRequest
from ..model.oql_query_application_object_response import OqlQueryApplicationObjectResponse as OqlQueryApplicationObjectResponse
from ..model.search_application_object_request import SearchApplicationObjectRequest as SearchApplicationObjectRequest
from ..model.search_application_object_response import SearchApplicationObjectResponse as SearchApplicationObjectResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationObject:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def oql_query(self, request: OqlQueryApplicationObjectRequest, option: RequestOption | None = None) -> OqlQueryApplicationObjectResponse: ...
    async def aoql_query(self, request: OqlQueryApplicationObjectRequest, option: RequestOption | None = None) -> OqlQueryApplicationObjectResponse: ...
    def search(self, request: SearchApplicationObjectRequest, option: RequestOption | None = None) -> SearchApplicationObjectResponse: ...
    async def asearch(self, request: SearchApplicationObjectRequest, option: RequestOption | None = None) -> SearchApplicationObjectResponse: ...
