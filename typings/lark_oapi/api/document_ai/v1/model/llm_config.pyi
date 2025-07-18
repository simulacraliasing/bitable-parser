from .llm_message import LlmMessage as LlmMessage
from lark_oapi.core.construct import init as init

class LlmConfig:
    model: str | None
    messages: list[LlmMessage] | None
    max_tokens: int | None
    message_type: str | None
    n: int | None
    temperature: float | None
    presence_penalty: float | None
    frequency_penalty: float | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> LlmConfigBuilder: ...

class LlmConfigBuilder:
    def __init__(self) -> None: ...
    def model(self, model: str) -> LlmConfigBuilder: ...
    def messages(self, messages: list[LlmMessage]) -> LlmConfigBuilder: ...
    def max_tokens(self, max_tokens: int) -> LlmConfigBuilder: ...
    def message_type(self, message_type: str) -> LlmConfigBuilder: ...
    def n(self, n: int) -> LlmConfigBuilder: ...
    def temperature(self, temperature: float) -> LlmConfigBuilder: ...
    def presence_penalty(self, presence_penalty: float) -> LlmConfigBuilder: ...
    def frequency_penalty(self, frequency_penalty: float) -> LlmConfigBuilder: ...
    def build(self) -> LlmConfig: ...
