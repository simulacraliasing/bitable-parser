from .execute_application_flow_response_body import ExecuteApplicationFlowResponseBody as ExecuteApplicationFlowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ExecuteApplicationFlowResponse(BaseResponse):
    data: ExecuteApplicationFlowResponseBody | None
    def __init__(self, d=None) -> None: ...
