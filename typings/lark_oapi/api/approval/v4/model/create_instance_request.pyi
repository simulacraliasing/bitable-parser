from .instance_create import InstanceCreate as InstanceCreate
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class CreateInstanceRequest(BaseRequest):
    request_body: InstanceCreate | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> CreateInstanceRequestBuilder: ...

class CreateInstanceRequestBuilder:
    def __init__(self) -> None: ...
    def request_body(self, request_body: InstanceCreate) -> CreateInstanceRequestBuilder: ...
    def build(self) -> CreateInstanceRequest: ...
