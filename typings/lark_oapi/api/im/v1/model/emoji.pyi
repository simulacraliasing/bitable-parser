from lark_oapi.core.construct import init as init

class Emoji:
    emoji_type: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EmojiBuilder: ...

class EmojiBuilder:
    def __init__(self) -> None: ...
    def emoji_type(self, emoji_type: str) -> EmojiBuilder: ...
    def build(self) -> Emoji: ...
