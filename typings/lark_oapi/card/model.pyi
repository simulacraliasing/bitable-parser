from lark_oapi.core.construct import init as init
from lark_oapi.core.model import RawRequest as RawRequest
from typing import Any

class Action:
    value: dict[str, Any]
    tag: str | None
    option: str | None
    timezone: str | None
    name: str | None
    form_value: dict[str, Any]
    input_value: str | None
    options: list[str] | None
    checked: bool | None
    def __init__(self, d=None) -> None: ...

class Card:
    open_id: str | None
    user_id: str | None
    tenant_key: str | None
    open_message_id: str | None
    open_chat_id: str | None
    token: str | None
    challenge: str | None
    type: str | None
    action: Action | None
    raw: RawRequest | None
    def __init__(self, d=None) -> None: ...
