from .assets import Assets as Assets
from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2HireReferralAccountAssetsUpdateV1Data:
    account_id: str | None
    assets: Assets | None
    modify_time: str | None
    def __init__(self, d=None) -> None: ...

class P2HireReferralAccountAssetsUpdateV1(EventContext):
    event: P2HireReferralAccountAssetsUpdateV1Data | None
    def __init__(self, d=None) -> None: ...
