from lark_oapi.core.construct import init as init

class GetAgentSkillRequestBody:
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetAgentSkillRequestBodyBuilder: ...

class GetAgentSkillRequestBodyBuilder:
    def __init__(self) -> None: ...
    def build(self) -> GetAgentSkillRequestBody: ...
