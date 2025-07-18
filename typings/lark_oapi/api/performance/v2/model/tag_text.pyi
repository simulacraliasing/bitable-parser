from lark_oapi.core.construct import init as init

class TagText:
    tag_text_id: str | None
    tag_text: str | None
    tag_richtext: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TagTextBuilder: ...

class TagTextBuilder:
    def __init__(self) -> None: ...
    def tag_text_id(self, tag_text_id: str) -> TagTextBuilder: ...
    def tag_text(self, tag_text: str) -> TagTextBuilder: ...
    def tag_richtext(self, tag_richtext: str) -> TagTextBuilder: ...
    def build(self) -> TagText: ...
