from .get_user_flow_response_body import GetUserFlowResponseBody as GetUserFlowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetUserFlowResponse(BaseResponse):
    data: GetUserFlowResponseBody | None
    def __init__(self, d=None) -> None: ...
