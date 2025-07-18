from .transfer_reason import TransferReason as TransferReason
from lark_oapi.core.construct import init as init

class QueryTransferReasonResponseBody:
    items: list[TransferReason] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryTransferReasonResponseBodyBuilder: ...

class QueryTransferReasonResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[TransferReason]) -> QueryTransferReasonResponseBodyBuilder: ...
    def build(self) -> QueryTransferReasonResponseBody: ...
