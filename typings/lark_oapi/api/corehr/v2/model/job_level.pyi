from .custom_field_data import CustomFieldData as CustomFieldData
from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class JobLevel:
    job_level_id: str | None
    level_order: int | None
    code: str | None
    name: list[I18n] | None
    description: list[I18n] | None
    active: bool | None
    custom_fields: list[CustomFieldData] | None
    job_grade: list[str] | None
    pathway_ids: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobLevelBuilder: ...

class JobLevelBuilder:
    def __init__(self) -> None: ...
    def job_level_id(self, job_level_id: str) -> JobLevelBuilder: ...
    def level_order(self, level_order: int) -> JobLevelBuilder: ...
    def code(self, code: str) -> JobLevelBuilder: ...
    def name(self, name: list[I18n]) -> JobLevelBuilder: ...
    def description(self, description: list[I18n]) -> JobLevelBuilder: ...
    def active(self, active: bool) -> JobLevelBuilder: ...
    def custom_fields(self, custom_fields: list[CustomFieldData]) -> JobLevelBuilder: ...
    def job_grade(self, job_grade: list[str]) -> JobLevelBuilder: ...
    def pathway_ids(self, pathway_ids: list[str]) -> JobLevelBuilder: ...
    def build(self) -> JobLevel: ...
