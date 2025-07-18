from .mailgroup import Mailgroup as Mailgroup
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchMailgroupRequest(BaseRequest):
    mailgroup_id: str | None
    request_body: Mailgroup | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchMailgroupRequestBuilder: ...

class PatchMailgroupRequestBuilder:
    def __init__(self) -> None: ...
    def mailgroup_id(self, mailgroup_id: str) -> PatchMailgroupRequestBuilder: ...
    def request_body(self, request_body: Mailgroup) -> PatchMailgroupRequestBuilder: ...
    def build(self) -> PatchMailgroupRequest: ...
