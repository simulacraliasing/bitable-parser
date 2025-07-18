from .restore_flow_instance_pre_hire_response_body import RestoreFlowInstancePreHireResponseBody as RestoreFlowInstancePreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RestoreFlowInstancePreHireResponse(BaseResponse):
    data: RestoreFlowInstancePreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
