from lark_oapi.core.construct import init as init

class MyAiSearchDefinitionScenarioContext:
    tool_raw_instruction: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MyAiSearchDefinitionScenarioContextBuilder: ...

class MyAiSearchDefinitionScenarioContextBuilder:
    def __init__(self) -> None: ...
    def tool_raw_instruction(self, tool_raw_instruction: str) -> MyAiSearchDefinitionScenarioContextBuilder: ...
    def build(self) -> MyAiSearchDefinitionScenarioContext: ...
