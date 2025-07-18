from .i18n import I18n as I18n
from lark_oapi.core.construct import init as init

class JobVersionData:
    job_id: str | None
    job_version_id: str | None
    job_names: list[I18n] | None
    effective_date: str | None
    expiration_date: str | None
    active: bool | None
    descriptions: list[I18n] | None
    code: str | None
    job_titles: list[I18n] | None
    job_family_ids: list[str] | None
    job_level_ids: list[str] | None
    pathway_id: str | None
    working_hours_type_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobVersionDataBuilder: ...

class JobVersionDataBuilder:
    def __init__(self) -> None: ...
    def job_id(self, job_id: str) -> JobVersionDataBuilder: ...
    def job_version_id(self, job_version_id: str) -> JobVersionDataBuilder: ...
    def job_names(self, job_names: list[I18n]) -> JobVersionDataBuilder: ...
    def effective_date(self, effective_date: str) -> JobVersionDataBuilder: ...
    def expiration_date(self, expiration_date: str) -> JobVersionDataBuilder: ...
    def active(self, active: bool) -> JobVersionDataBuilder: ...
    def descriptions(self, descriptions: list[I18n]) -> JobVersionDataBuilder: ...
    def code(self, code: str) -> JobVersionDataBuilder: ...
    def job_titles(self, job_titles: list[I18n]) -> JobVersionDataBuilder: ...
    def job_family_ids(self, job_family_ids: list[str]) -> JobVersionDataBuilder: ...
    def job_level_ids(self, job_level_ids: list[str]) -> JobVersionDataBuilder: ...
    def pathway_id(self, pathway_id: str) -> JobVersionDataBuilder: ...
    def working_hours_type_id(self, working_hours_type_id: str) -> JobVersionDataBuilder: ...
    def build(self) -> JobVersionData: ...
