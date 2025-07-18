from ..model.get_currency_request import GetCurrencyRequest as GetCurrencyRequest
from ..model.get_currency_response import GetCurrencyResponse as GetCurrencyResponse
from ..model.list_currency_request import ListCurrencyRequest as ListCurrencyRequest
from ..model.list_currency_response import ListCurrencyResponse as ListCurrencyResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Currency:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetCurrencyRequest, option: RequestOption | None = None) -> GetCurrencyResponse: ...
    async def aget(self, request: GetCurrencyRequest, option: RequestOption | None = None) -> GetCurrencyResponse: ...
    def list(self, request: ListCurrencyRequest, option: RequestOption | None = None) -> ListCurrencyResponse: ...
    async def alist(self, request: ListCurrencyRequest, option: RequestOption | None = None) -> ListCurrencyResponse: ...
