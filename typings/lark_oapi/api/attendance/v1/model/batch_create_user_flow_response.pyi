from .batch_create_user_flow_response_body import BatchCreateUserFlowResponseBody as BatchCreateUserFlowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateUserFlowResponse(BaseResponse):
    data: BatchCreateUserFlowResponseBody | None
    def __init__(self, d=None) -> None: ...
