from .get_application_environment_variable_response_body import GetApplicationEnvironmentVariableResponseBody as GetApplicationEnvironmentVariableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationEnvironmentVariableResponse(BaseResponse):
    data: GetApplicationEnvironmentVariableResponseBody | None
    def __init__(self, d=None) -> None: ...
