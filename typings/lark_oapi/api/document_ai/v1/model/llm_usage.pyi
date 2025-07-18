from lark_oapi.core.construct import init as init

class LlmUsage:
    prompt_tokens: int | None
    completion_tokens: int | None
    total_tokens: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LlmUsageBuilder: ...

class LlmUsageBuilder:
    def __init__(self) -> None: ...
    def prompt_tokens(self, prompt_tokens: int) -> LlmUsageBuilder: ...
    def completion_tokens(self, completion_tokens: int) -> LlmUsageBuilder: ...
    def total_tokens(self, total_tokens: int) -> LlmUsageBuilder: ...
    def build(self) -> LlmUsage: ...
