from ..model.get_work_city_request import GetWorkCityRequest as GetWorkCityRequest
from ..model.get_work_city_response import GetWorkCityResponse as GetWorkCityResponse
from ..model.list_work_city_request import ListWorkCityRequest as ListWorkCityRequest
from ..model.list_work_city_response import ListWorkCityResponse as ListWorkCityResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class WorkCity:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetWorkCityRequest, option: RequestOption | None = None) -> GetWorkCityResponse: ...
    async def aget(self, request: GetWorkCityRequest, option: RequestOption | None = None) -> GetWorkCityResponse: ...
    def list(self, request: ListWorkCityRequest, option: RequestOption | None = None) -> ListWorkCityResponse: ...
    async def alist(self, request: ListWorkCityRequest, option: RequestOption | None = None) -> ListWorkCityResponse: ...
