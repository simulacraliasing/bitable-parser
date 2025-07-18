from lark_oapi.core.construct import init as init

class Mention:
    key: str | None
    id: str | None
    id_type: str | None
    name: str | None
    tenant_key: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> MentionBuilder: ...

class MentionBuilder:
    def __init__(self) -> None: ...
    def key(self, key: str) -> MentionBuilder: ...
    def id(self, id: str) -> MentionBuilder: ...
    def id_type(self, id_type: str) -> MentionBuilder: ...
    def name(self, name: str) -> MentionBuilder: ...
    def tenant_key(self, tenant_key: str) -> MentionBuilder: ...
    def build(self) -> Mention: ...
