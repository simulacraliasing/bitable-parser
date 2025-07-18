from lark_oapi.core.construct import init as init

class CreateAilySessionRunRequestBody:
    app_id: str | None
    skill_id: str | None
    skill_input: str | None
    metadata: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateAilySessionRunRequestBodyBuilder: ...

class CreateAilySessionRunRequestBodyBuilder:
    def __init__(self) -> None: ...
    def app_id(self, app_id: str) -> CreateAilySessionRunRequestBodyBuilder: ...
    def skill_id(self, skill_id: str) -> CreateAilySessionRunRequestBodyBuilder: ...
    def skill_input(self, skill_input: str) -> CreateAilySessionRunRequestBodyBuilder: ...
    def metadata(self, metadata: str) -> CreateAilySessionRunRequestBodyBuilder: ...
    def build(self) -> CreateAilySessionRunRequestBody: ...
