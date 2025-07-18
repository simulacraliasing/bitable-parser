from lark_oapi.core.construct import init as init

class NlsModelConfig:
    model_name: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> NlsModelConfigBuilder: ...

class NlsModelConfigBuilder:
    def __init__(self) -> None: ...
    def model_name(self, model_name: str) -> NlsModelConfigBuilder: ...
    def build(self) -> NlsModelConfig: ...
