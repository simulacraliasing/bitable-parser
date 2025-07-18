from .instance_cancel import InstanceCancel as InstanceCancel
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CancelInstanceRequest(BaseRequest):
    user_id_type: str | None
    request_body: InstanceCancel | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CancelInstanceRequestBuilder: ...

class CancelInstanceRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> CancelInstanceRequestBuilder: ...
    def request_body(self, request_body: InstanceCancel) -> CancelInstanceRequestBuilder: ...
    def build(self) -> CancelInstanceRequest: ...
