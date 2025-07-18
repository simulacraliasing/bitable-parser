from ..model.get_application_environment_variable_request import GetApplicationEnvironmentVariableRequest as GetApplicationEnvironmentVariableRequest
from ..model.get_application_environment_variable_response import GetApplicationEnvironmentVariableResponse as GetApplicationEnvironmentVariableResponse
from ..model.query_application_environment_variable_request import QueryApplicationEnvironmentVariableRequest as QueryApplicationEnvironmentVariableRequest
from ..model.query_application_environment_variable_response import QueryApplicationEnvironmentVariableResponse as QueryApplicationEnvironmentVariableResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ApplicationEnvironmentVariable:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetApplicationEnvironmentVariableRequest, option: RequestOption | None = None) -> GetApplicationEnvironmentVariableResponse: ...
    async def aget(self, request: GetApplicationEnvironmentVariableRequest, option: RequestOption | None = None) -> GetApplicationEnvironmentVariableResponse: ...
    def query(self, request: QueryApplicationEnvironmentVariableRequest, option: RequestOption | None = None) -> QueryApplicationEnvironmentVariableResponse: ...
    async def aquery(self, request: QueryApplicationEnvironmentVariableRequest, option: RequestOption | None = None) -> QueryApplicationEnvironmentVariableResponse: ...
