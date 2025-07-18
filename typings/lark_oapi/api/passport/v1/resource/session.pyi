from ..model.logout_session_request import LogoutSessionRequest as LogoutSessionRequest
from ..model.logout_session_response import LogoutSessionResponse as LogoutSessionResponse
from ..model.query_session_request import QuerySessionRequest as QuerySessionRequest
from ..model.query_session_response import QuerySessionResponse as QuerySessionResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Session:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def logout(self, request: LogoutSessionRequest, option: RequestOption | None = None) -> LogoutSessionResponse: ...
    async def alogout(self, request: LogoutSessionRequest, option: RequestOption | None = None) -> LogoutSessionResponse: ...
    def query(self, request: QuerySessionRequest, option: RequestOption | None = None) -> QuerySessionResponse: ...
    async def aquery(self, request: QuerySessionRequest, option: RequestOption | None = None) -> QuerySessionResponse: ...
