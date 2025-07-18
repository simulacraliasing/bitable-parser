from .emoji import Emoji as Emoji
from .operator import Operator as Operator
from lark_oapi.core.construct import init as init

class CreateMessageReactionResponseBody:
    reaction_id: str | None
    operator: Operator | None
    action_time: int | None
    reaction_type: Emoji | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateMessageReactionResponseBodyBuilder: ...

class CreateMessageReactionResponseBodyBuilder:
    def __init__(self) -> None: ...
    def reaction_id(self, reaction_id: str) -> CreateMessageReactionResponseBodyBuilder: ...
    def operator(self, operator: Operator) -> CreateMessageReactionResponseBodyBuilder: ...
    def action_time(self, action_time: int) -> CreateMessageReactionResponseBodyBuilder: ...
    def reaction_type(self, reaction_type: Emoji) -> CreateMessageReactionResponseBodyBuilder: ...
    def build(self) -> CreateMessageReactionResponseBody: ...
