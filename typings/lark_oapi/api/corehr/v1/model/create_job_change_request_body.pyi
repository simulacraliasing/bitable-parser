from .transfer_info import TransferInfo as TransferInfo
from lark_oapi.core.construct import init as init

class CreateJobChangeRequestBody:
    transfer_mode: int | None
    employment_id: str | None
    transfer_type_unique_identifier: str | None
    flow_id: str | None
    effective_date: str | None
    transfer_info: TransferInfo | None
    transfer_key: str | None
    initiator_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateJobChangeRequestBodyBuilder: ...

class CreateJobChangeRequestBodyBuilder:
    def __init__(self) -> None: ...
    def transfer_mode(self, transfer_mode: int) -> CreateJobChangeRequestBodyBuilder: ...
    def employment_id(self, employment_id: str) -> CreateJobChangeRequestBodyBuilder: ...
    def transfer_type_unique_identifier(self, transfer_type_unique_identifier: str) -> CreateJobChangeRequestBodyBuilder: ...
    def flow_id(self, flow_id: str) -> CreateJobChangeRequestBodyBuilder: ...
    def effective_date(self, effective_date: str) -> CreateJobChangeRequestBodyBuilder: ...
    def transfer_info(self, transfer_info: TransferInfo) -> CreateJobChangeRequestBodyBuilder: ...
    def transfer_key(self, transfer_key: str) -> CreateJobChangeRequestBodyBuilder: ...
    def initiator_id(self, initiator_id: str) -> CreateJobChangeRequestBodyBuilder: ...
    def build(self) -> CreateJobChangeRequestBody: ...
