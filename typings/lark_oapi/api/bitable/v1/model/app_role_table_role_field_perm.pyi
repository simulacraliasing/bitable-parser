from lark_oapi.core.construct import init as init

class AppRoleTableRoleFieldPerm:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AppRoleTableRoleFieldPermBuilder: ...

class AppRoleTableRoleFieldPermBuilder:
    def __init__(self) -> None: ...
    def build(self) -> AppRoleTableRoleFieldPerm: ...
