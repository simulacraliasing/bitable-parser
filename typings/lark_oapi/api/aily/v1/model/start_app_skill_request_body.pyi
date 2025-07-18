from .skill_global_variable import SkillGlobalVariable as SkillGlobalVariable
from lark_oapi.core.construct import init as init

class StartAppSkillRequestBody:
    global_variable: SkillGlobalVariable | None
    input: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> StartAppSkillRequestBodyBuilder: ...

class StartAppSkillRequestBodyBuilder:
    def __init__(self) -> None: ...
    def global_variable(self, global_variable: SkillGlobalVariable) -> StartAppSkillRequestBodyBuilder: ...
    def input(self, input: str) -> StartAppSkillRequestBodyBuilder: ...
    def build(self) -> StartAppSkillRequestBody: ...
