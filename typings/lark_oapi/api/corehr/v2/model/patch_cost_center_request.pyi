from .patch_cost_center_request_body import PatchCostCenterRequestBody as PatchCostCenterRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchCostCenterRequest(BaseRequest):
    user_id_type: str | None
    cost_center_id: str | None
    request_body: PatchCostCenterRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchCostCenterRequestBuilder: ...

class PatchCostCenterRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> PatchCostCenterRequestBuilder: ...
    def cost_center_id(self, cost_center_id: str) -> PatchCostCenterRequestBuilder: ...
    def request_body(self, request_body: PatchCostCenterRequestBody) -> PatchCostCenterRequestBuilder: ...
    def build(self) -> PatchCostCenterRequest: ...
