from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext
from typing import Any

class CallBackOperator:
    tenant_key: str | None
    user_id: str | None
    open_id: str | None
    union_id: str | None
    def __init__(self, d=None) -> None: ...

class CallBackContext:
    url: str | None
    preview_token: str | None
    open_message_id: str | None
    open_chat_id: str | None
    def __init__(self, d=None) -> None: ...

class CallBackAction:
    value: dict[str, Any] | None
    tag: str | None
    option: str | None
    timezone: str | None
    name: str | None
    form_value: dict[str, Any] | None
    input_value: str | None
    options: list[str] | None
    checked: bool | None
    def __init__(self, d=None) -> None: ...

class P2CardActionTriggerData:
    operator: CallBackOperator | None
    token: str | None
    action: CallBackAction | None
    host: str | None
    delivery_type: str | None
    context: CallBackContext | None
    def __init__(self, d=None) -> None: ...

class P2CardActionTrigger(EventContext):
    event: P2CardActionTriggerData | None
    def __init__(self, d=None) -> None: ...

class CallBackToast:
    type: str | None
    content: str | None
    i18n: dict[str, str] | None
    def __init__(self, d=None) -> None: ...

class CallBackCard:
    type: str | None
    data: Any | None
    def __init__(self, d=None) -> None: ...

class P2CardActionTriggerResponse:
    toast: CallBackToast | None
    card: CallBackCard | None
    def __init__(self, d=None) -> None: ...
