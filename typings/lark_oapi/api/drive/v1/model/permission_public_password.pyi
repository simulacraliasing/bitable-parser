from lark_oapi.core.construct import init as init

class PermissionPublicPassword:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PermissionPublicPasswordBuilder: ...

class PermissionPublicPasswordBuilder:
    def __init__(self) -> None: ...
    def build(self) -> PermissionPublicPassword: ...
