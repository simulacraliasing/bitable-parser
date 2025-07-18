from .transfer_info import TransferInfo as TransferInfo
from lark_oapi.core.construct import init as init

class CreateJobChangeResponseBody:
    job_change_id: str | None
    employment_id: str | None
    status: int | None
    transfer_type_unique_identifier: str | None
    transfer_reason_unique_identifier: str | None
    process_id: str | None
    effective_date: str | None
    created_time: str | None
    transfer_info: TransferInfo | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateJobChangeResponseBodyBuilder: ...

class CreateJobChangeResponseBodyBuilder:
    def __init__(self) -> None: ...
    def job_change_id(self, job_change_id: str) -> CreateJobChangeResponseBodyBuilder: ...
    def employment_id(self, employment_id: str) -> CreateJobChangeResponseBodyBuilder: ...
    def status(self, status: int) -> CreateJobChangeResponseBodyBuilder: ...
    def transfer_type_unique_identifier(self, transfer_type_unique_identifier: str) -> CreateJobChangeResponseBodyBuilder: ...
    def transfer_reason_unique_identifier(self, transfer_reason_unique_identifier: str) -> CreateJobChangeResponseBodyBuilder: ...
    def process_id(self, process_id: str) -> CreateJobChangeResponseBodyBuilder: ...
    def effective_date(self, effective_date: str) -> CreateJobChangeResponseBodyBuilder: ...
    def created_time(self, created_time: str) -> CreateJobChangeResponseBodyBuilder: ...
    def transfer_info(self, transfer_info: TransferInfo) -> CreateJobChangeResponseBodyBuilder: ...
    def build(self) -> CreateJobChangeResponseBody: ...
