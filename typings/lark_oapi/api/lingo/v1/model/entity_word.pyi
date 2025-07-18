from lark_oapi.core.construct import init as init

class EntityWord:
    name: str | None
    aliases: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EntityWordBuilder: ...

class EntityWordBuilder:
    def __init__(self) -> None: ...
    def name(self, name: str) -> EntityWordBuilder: ...
    def aliases(self, aliases: list[str]) -> EntityWordBuilder: ...
    def build(self) -> EntityWord: ...
