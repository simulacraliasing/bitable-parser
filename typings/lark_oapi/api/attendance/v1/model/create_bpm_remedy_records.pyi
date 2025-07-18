from .remedy_record import RemedyRecord as RemedyRecord
from lark_oapi.core.construct import init as init

class CreateBpmRemedyRecords:
    user_id: str | None
    remedy_records: list[RemedyRecord] | None
    remedy_reason: str | None
    custom_form_data: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateBpmRemedyRecordsBuilder: ...

class CreateBpmRemedyRecordsBuilder:
    def __init__(self) -> None: ...
    def user_id(self, user_id: str) -> CreateBpmRemedyRecordsBuilder: ...
    def remedy_records(self, remedy_records: list[RemedyRecord]) -> CreateBpmRemedyRecordsBuilder: ...
    def remedy_reason(self, remedy_reason: str) -> CreateBpmRemedyRecordsBuilder: ...
    def custom_form_data(self, custom_form_data: str) -> CreateBpmRemedyRecordsBuilder: ...
    def build(self) -> CreateBpmRemedyRecords: ...
