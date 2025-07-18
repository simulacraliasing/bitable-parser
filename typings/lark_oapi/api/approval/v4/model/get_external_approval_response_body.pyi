from .approval_create_external import ApprovalCreateExternal as ApprovalCreateExternal
from .approval_create_viewers import ApprovalCreateViewers as ApprovalCreateViewers
from .i18n_resource import I18nResource as I18nResource
from lark_oapi.core.construct import init as init

class GetExternalApprovalResponseBody:
    approval_name: str | None
    approval_code: str | None
    group_code: str | None
    group_name: str | None
    description: str | None
    external: ApprovalCreateExternal | None
    viewers: list[ApprovalCreateViewers] | None
    i18n_resources: list[I18nResource] | None
    managers: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetExternalApprovalResponseBodyBuilder: ...

class GetExternalApprovalResponseBodyBuilder:
    def __init__(self) -> None: ...
    def approval_name(self, approval_name: str) -> GetExternalApprovalResponseBodyBuilder: ...
    def approval_code(self, approval_code: str) -> GetExternalApprovalResponseBodyBuilder: ...
    def group_code(self, group_code: str) -> GetExternalApprovalResponseBodyBuilder: ...
    def group_name(self, group_name: str) -> GetExternalApprovalResponseBodyBuilder: ...
    def description(self, description: str) -> GetExternalApprovalResponseBodyBuilder: ...
    def external(self, external: ApprovalCreateExternal) -> GetExternalApprovalResponseBodyBuilder: ...
    def viewers(self, viewers: list[ApprovalCreateViewers]) -> GetExternalApprovalResponseBodyBuilder: ...
    def i18n_resources(self, i18n_resources: list[I18nResource]) -> GetExternalApprovalResponseBodyBuilder: ...
    def managers(self, managers: list[str]) -> GetExternalApprovalResponseBodyBuilder: ...
    def build(self) -> GetExternalApprovalResponseBody: ...
