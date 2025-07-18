from lark_oapi.core.construct import init as init

class BatchDeleteMailgroupPermissionMemberRequestBody:
    permission_member_id_list: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchDeleteMailgroupPermissionMemberRequestBodyBuilder: ...

class BatchDeleteMailgroupPermissionMemberRequestBodyBuilder:
    def __init__(self) -> None: ...
    def permission_member_id_list(self, permission_member_id_list: list[str]) -> BatchDeleteMailgroupPermissionMemberRequestBodyBuilder: ...
    def build(self) -> BatchDeleteMailgroupPermissionMemberRequestBody: ...
