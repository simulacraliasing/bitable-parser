from .app_role_table_role_rec_rule import AppRoleTableRoleRecRule as AppRoleTableRoleRecRule
from lark_oapi.core.construct import init as init

class AppRoleTableRole:
    table_perm: int | None
    table_name: str | None
    table_id: str | None
    rec_rule: AppRoleTableRoleRecRule | None
    field_perm: dict[str, int] | None
    allow_add_record: bool | None
    allow_delete_record: bool | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppRoleTableRoleBuilder: ...

class AppRoleTableRoleBuilder:
    def __init__(self) -> None: ...
    def table_perm(self, table_perm: int) -> AppRoleTableRoleBuilder: ...
    def table_name(self, table_name: str) -> AppRoleTableRoleBuilder: ...
    def table_id(self, table_id: str) -> AppRoleTableRoleBuilder: ...
    def rec_rule(self, rec_rule: AppRoleTableRoleRecRule) -> AppRoleTableRoleBuilder: ...
    def field_perm(self, field_perm: dict[str, int]) -> AppRoleTableRoleBuilder: ...
    def allow_add_record(self, allow_add_record: bool) -> AppRoleTableRoleBuilder: ...
    def allow_delete_record(self, allow_delete_record: bool) -> AppRoleTableRoleBuilder: ...
    def build(self) -> AppRoleTableRole: ...
