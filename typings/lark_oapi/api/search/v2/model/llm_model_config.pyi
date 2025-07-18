from lark_oapi.core.construct import init as init

class LlmModelConfig:
    model_name: str | None
    prompt: str | None
    max_token: int | None
    temperature: float | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LlmModelConfigBuilder: ...

class LlmModelConfigBuilder:
    def __init__(self) -> None: ...
    def model_name(self, model_name: str) -> LlmModelConfigBuilder: ...
    def prompt(self, prompt: str) -> LlmModelConfigBuilder: ...
    def max_token(self, max_token: int) -> LlmModelConfigBuilder: ...
    def temperature(self, temperature: float) -> LlmModelConfigBuilder: ...
    def build(self) -> LlmModelConfig: ...
