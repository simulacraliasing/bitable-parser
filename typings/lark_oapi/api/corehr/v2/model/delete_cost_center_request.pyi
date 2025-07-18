from .delete_cost_center_request_body import DeleteCostCenterRequestBody as DeleteCostCenterRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class DeleteCostCenterRequest(BaseRequest):
    cost_center_id: str | None
    request_body: DeleteCostCenterRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> DeleteCostCenterRequestBuilder: ...

class DeleteCostCenterRequestBuilder:
    def __init__(self) -> None: ...
    def cost_center_id(self, cost_center_id: str) -> DeleteCostCenterRequestBuilder: ...
    def request_body(self, request_body: DeleteCostCenterRequestBody) -> DeleteCostCenterRequestBuilder: ...
    def build(self) -> DeleteCostCenterRequest: ...
