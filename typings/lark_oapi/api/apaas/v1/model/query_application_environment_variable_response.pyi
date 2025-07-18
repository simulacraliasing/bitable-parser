from .query_application_environment_variable_response_body import QueryApplicationEnvironmentVariableResponseBody as QueryApplicationEnvironmentVariableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryApplicationEnvironmentVariableResponse(BaseResponse):
    data: QueryApplicationEnvironmentVariableResponseBody | None
    def __init__(self, d=None) -> None: ...
