from ..model.get_authorize_request import GetAuthorizeRequest as GetAuthorizeRequest
from ..model.get_authorize_response import GetAuthorizeResponse as GetAuthorizeResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify

class Authorize:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetAuthorizeRequest, option: RequestOption | None = None) -> GetAuthorizeResponse: ...
