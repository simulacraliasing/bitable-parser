from .grant import Grant as Grant
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class UpdateBadgeGrantRequest(BaseRequest):
    user_id_type: str | None
    department_id_type: str | None
    badge_id: str | None
    grant_id: str | None
    request_body: Grant | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> UpdateBadgeGrantRequestBuilder: ...

class UpdateBadgeGrantRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> UpdateBadgeGrantRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> UpdateBadgeGrantRequestBuilder: ...
    def badge_id(self, badge_id: str) -> UpdateBadgeGrantRequestBuilder: ...
    def grant_id(self, grant_id: str) -> UpdateBadgeGrantRequestBuilder: ...
    def request_body(self, request_body: Grant) -> UpdateBadgeGrantRequestBuilder: ...
    def build(self) -> UpdateBadgeGrantRequest: ...
