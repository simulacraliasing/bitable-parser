from ..model.search_basic_info_currency_request import SearchBasicInfoCurrencyRequest as SearchBasicInfoCurrencyRequest
from ..model.search_basic_info_currency_response import SearchBasicInfoCurrencyResponse as SearchBasicInfoCurrencyResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class BasicInfoCurrency:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def search(self, request: SearchBasicInfoCurrencyRequest, option: RequestOption | None = None) -> SearchBasicInfoCurrencyResponse: ...
    async def asearch(self, request: SearchBasicInfoCurrencyRequest, option: RequestOption | None = None) -> SearchBasicInfoCurrencyResponse: ...
