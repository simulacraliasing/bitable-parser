from .patch_application_contacts_range_request_body import PatchApplicationContactsRangeRequestBody as PatchApplicationContactsRangeRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class PatchApplicationContactsRangeRequest(BaseRequest):
    user_id_type: str | None
    department_id_type: str | None
    app_id: str | None
    request_body: PatchApplicationContactsRangeRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> PatchApplicationContactsRangeRequestBuilder: ...

class PatchApplicationContactsRangeRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> PatchApplicationContactsRangeRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> PatchApplicationContactsRangeRequestBuilder: ...
    def app_id(self, app_id: str) -> PatchApplicationContactsRangeRequestBuilder: ...
    def request_body(self, request_body: PatchApplicationContactsRangeRequestBody) -> PatchApplicationContactsRangeRequestBuilder: ...
    def build(self) -> PatchApplicationContactsRangeRequest: ...
