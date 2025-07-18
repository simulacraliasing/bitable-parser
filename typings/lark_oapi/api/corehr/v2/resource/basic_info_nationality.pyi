from ..model.search_basic_info_nationality_request import SearchBasicInfoNationalityRequest as SearchBasicInfoNationalityRequest
from ..model.search_basic_info_nationality_response import SearchBasicInfoNationalityResponse as SearchBasicInfoNationalityResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class BasicInfoNationality:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def search(self, request: SearchBasicInfoNationalityRequest, option: RequestOption | None = None) -> SearchBasicInfoNationalityResponse: ...
    async def asearch(self, request: SearchBasicInfoNationalityRequest, option: RequestOption | None = None) -> SearchBasicInfoNationalityResponse: ...
