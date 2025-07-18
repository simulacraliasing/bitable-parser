from lark_oapi.core.construct import init as init

class CheckWhiteBlackListApplicationVisibilityRequestBody:
    user_ids: list[str] | None
    department_ids: list[str] | None
    group_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder: ...

class CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder:
    def __init__(self) -> None: ...
    def user_ids(self, user_ids: list[str]) -> CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder: ...
    def department_ids(self, department_ids: list[str]) -> CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder: ...
    def group_ids(self, group_ids: list[str]) -> CheckWhiteBlackListApplicationVisibilityRequestBodyBuilder: ...
    def build(self) -> CheckWhiteBlackListApplicationVisibilityRequestBody: ...
