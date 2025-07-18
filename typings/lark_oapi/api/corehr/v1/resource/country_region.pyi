from ..model.get_country_region_request import GetCountryRegionRequest as GetCountryRegionRequest
from ..model.get_country_region_response import GetCountryRegionResponse as GetCountryRegionResponse
from ..model.list_country_region_request import ListCountryRegionRequest as ListCountryRegionRequest
from ..model.list_country_region_response import ListCountryRegionResponse as ListCountryRegionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CountryRegion:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetCountryRegionRequest, option: RequestOption | None = None) -> GetCountryRegionResponse: ...
    async def aget(self, request: GetCountryRegionRequest, option: RequestOption | None = None) -> GetCountryRegionResponse: ...
    def list(self, request: ListCountryRegionRequest, option: RequestOption | None = None) -> ListCountryRegionResponse: ...
    async def alist(self, request: ListCountryRegionRequest, option: RequestOption | None = None) -> ListCountryRegionResponse: ...
