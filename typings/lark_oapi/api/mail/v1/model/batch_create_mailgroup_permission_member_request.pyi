from .batch_create_mailgroup_permission_member_request_body import BatchCreateMailgroupPermissionMemberRequestBody as BatchCreateMailgroupPermissionMemberRequestBody
from lark_oapi.core.enum import AccessTokenType as AccessTokenType, HttpMethod as HttpMethod
from lark_oapi.core.model import BaseRequest as BaseRequest

class BatchCreateMailgroupPermissionMemberRequest(BaseRequest):
    user_id_type: str | None
    department_id_type: str | None
    mailgroup_id: str | None
    request_body: BatchCreateMailgroupPermissionMemberRequestBody | None
    def __init__(self) -> None: ...
    @staticmethod
    def builder() -> BatchCreateMailgroupPermissionMemberRequestBuilder: ...

class BatchCreateMailgroupPermissionMemberRequestBuilder:
    def __init__(self) -> None: ...
    def user_id_type(self, user_id_type: str) -> BatchCreateMailgroupPermissionMemberRequestBuilder: ...
    def department_id_type(self, department_id_type: str) -> BatchCreateMailgroupPermissionMemberRequestBuilder: ...
    def mailgroup_id(self, mailgroup_id: str) -> BatchCreateMailgroupPermissionMemberRequestBuilder: ...
    def request_body(self, request_body: BatchCreateMailgroupPermissionMemberRequestBody) -> BatchCreateMailgroupPermissionMemberRequestBuilder: ...
    def build(self) -> BatchCreateMailgroupPermissionMemberRequest: ...
