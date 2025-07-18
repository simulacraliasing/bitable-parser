from lark_oapi.core.construct import init as init

class GroupVisibleScope:
    visible_scope_type: str | None
    visible_users: list[str] | None
    visible_departments: list[str] | None
    scene_types: list[int] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GroupVisibleScopeBuilder: ...

class GroupVisibleScopeBuilder:
    def __init__(self) -> None: ...
    def visible_scope_type(self, visible_scope_type: str) -> GroupVisibleScopeBuilder: ...
    def visible_users(self, visible_users: list[str]) -> GroupVisibleScopeBuilder: ...
    def visible_departments(self, visible_departments: list[str]) -> GroupVisibleScopeBuilder: ...
    def scene_types(self, scene_types: list[int]) -> GroupVisibleScopeBuilder: ...
    def build(self) -> GroupVisibleScope: ...
