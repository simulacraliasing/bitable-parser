from lark_oapi.core.construct import init as init

class CreateFunctionalRoleResponseBody:
    role_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateFunctionalRoleResponseBodyBuilder: ...

class CreateFunctionalRoleResponseBodyBuilder:
    def __init__(self) -> None: ...
    def role_id(self, role_id: str) -> CreateFunctionalRoleResponseBodyBuilder: ...
    def build(self) -> CreateFunctionalRoleResponseBody: ...
