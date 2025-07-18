from .patch_reserve_config_form_request_body import PatchReserveConfigFormRequestBody as PatchReserveConfigFormRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchReserveConfigFormRequest(BaseRequest):
    user_id_type: str | None
    reserve_config_id: str | None
    request_body: PatchReserveConfigFormRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchReserveConfigFormRequestBuilder: ...

class PatchReserveConfigFormRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> PatchReserveConfigFormRequestBuilder: ...
    def reserve_config_id(self, reserve_config_id: str) -> PatchReserveConfigFormRequestBuilder: ...
    def request_body(self, request_body: PatchReserveConfigFormRequestBody) -> PatchReserveConfigFormRequestBuilder: ...
    def build(self) -> PatchReserveConfigFormRequest: ...
