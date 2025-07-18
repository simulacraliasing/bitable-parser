from .aily_knowledge_message import AilyKnowledgeMessage as AilyKnowledgeMessage
from lark_oapi.core.construct import init as init

class AskAppKnowledgeRequestBody:
    message: AilyKnowledgeMessage | None
    data_asset_ids: list[str] | None
    data_asset_tag_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AskAppKnowledgeRequestBodyBuilder: ...

class AskAppKnowledgeRequestBodyBuilder:
    def __init__(self) -> None: ...
    def message(self, message: AilyKnowledgeMessage) -> AskAppKnowledgeRequestBodyBuilder: ...
    def data_asset_ids(self, data_asset_ids: list[str]) -> AskAppKnowledgeRequestBodyBuilder: ...
    def data_asset_tag_ids(self, data_asset_tag_ids: list[str]) -> AskAppKnowledgeRequestBodyBuilder: ...
    def build(self) -> AskAppKnowledgeRequestBody: ...
