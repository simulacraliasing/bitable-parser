from .batch_del_user_flow_response_body import BatchDelUserFlowResponseBody as BatchDelUserFlowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDelUserFlowResponse(BaseResponse):
    data: BatchDelUserFlowResponseBody | None
    def __init__(self, d=None) -> None: ...
