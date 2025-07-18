from .invoke_application_function_response_body import InvokeApplicationFunctionResponseBody as InvokeApplicationFunctionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class InvokeApplicationFunctionResponse(BaseResponse):
    data: InvokeApplicationFunctionResponseBody | None
    def __init__(self, d=None) -> None: ...
