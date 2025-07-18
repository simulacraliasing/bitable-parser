from .workforce_plan_detail_req import WorkforcePlanDetailReq as WorkforcePlanDetailReq
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchSaveWorkforcePlanDetailRowRequest(BaseRequest):
    request_body: WorkforcePlanDetailReq | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchSaveWorkforcePlanDetailRowRequestBuilder: ...

class BatchSaveWorkforcePlanDetailRowRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: WorkforcePlanDetailReq) -> BatchSaveWorkforcePlanDetailRowRequestBuilder: ...
    def build(self) -> BatchSaveWorkforcePlanDetailRowRequest: ...
