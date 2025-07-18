from lark_oapi.core.construct import init as init

class AilySender:
    entity_id: str | None
    identity_provider: str | None
    sender_type: str | None
    aily_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AilySenderBuilder: ...

class AilySenderBuilder:
    def __init__(self) -> None: ...
    def entity_id(self, entity_id: str) -> AilySenderBuilder: ...
    def identity_provider(self, identity_provider: str) -> AilySenderBuilder: ...
    def sender_type(self, sender_type: str) -> AilySenderBuilder: ...
    def aily_id(self, aily_id: str) -> AilySenderBuilder: ...
    def build(self) -> AilySender: ...
