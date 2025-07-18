from .social_plan_condition import SocialPlanCondition as SocialPlanCondition
from lark_oapi.core.construct import init as init

class SocialPlanScope:
    is_all: bool | None
    rules: list[list] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> SocialPlanScopeBuilder: ...

class SocialPlanScopeBuilder:
    def __init__(self) -> None: ...
    def is_all(self, is_all: bool) -> SocialPlanScopeBuilder: ...
    def rules(self, rules: list[list]) -> SocialPlanScopeBuilder: ...
    def build(self) -> SocialPlanScope: ...
