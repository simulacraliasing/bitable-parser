from lark_oapi.core.construct import init as init
from lark_oapi.event.callback.model.p2_card_action_trigger import CallBackCard as CallBackCard, CallBackContext as CallBackContext, CallBackOperator as CallBackOperator
from lark_oapi.event.context import EventContext as EventContext

class P2URLPreviewGetData:
    operator: CallBackOperator | None
    host: str | None
    context: CallBackContext | None
    def __init__(self, d=None) -> None: ...

class P2URLPreviewGet(EventContext):
    event: P2URLPreviewGetData | None
    def __init__(self, d=None) -> None: ...

class URLPreviewGetInlineURL:
    copy_url: str | None
    ios: str | None
    android: str | None
    pc: str | None
    web: str | None
    def __init__(self, d=None) -> None: ...

class URLPreviewGetInline:
    title: str | None
    i18n_title: dict[str, str] | None
    image_key: str | None
    url: URLPreviewGetInlineURL | None
    def __init__(self, d=None) -> None: ...

class P2URLPreviewGetResponse:
    inline: URLPreviewGetInline | None
    card: CallBackCard | None
    def __init__(self, d=None) -> None: ...
