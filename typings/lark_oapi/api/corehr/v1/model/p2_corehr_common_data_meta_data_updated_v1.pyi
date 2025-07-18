from lark_oapi.core.construct import init as init
from lark_oapi.event.context import EventContext as EventContext

class P2CorehrCommonDataMetaDataUpdatedV1Data:
    api_name: str | None
    field_changes: list[str] | None
    metadata_type: str | None
    enum_value_changes: list[str] | None
    def __init__(self, d=None) -> None: ...

class P2CorehrCommonDataMetaDataUpdatedV1(EventContext):
    event: P2CorehrCommonDataMetaDataUpdatedV1Data | None
    def __init__(self, d=None) -> None: ...
