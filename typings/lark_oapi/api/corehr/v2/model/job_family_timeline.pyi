from .job_family_version_data import JobFamilyVersionData as JobFamilyVersionData
from lark_oapi.core.construct import init as init

class JobFamilyTimeline:
    job_family_version_data: list[JobFamilyVersionData] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> JobFamilyTimelineBuilder: ...

class JobFamilyTimelineBuilder:
    def __init__(self) -> None: ...
    def job_family_version_data(self, job_family_version_data: list[JobFamilyVersionData]) -> JobFamilyTimelineBuilder: ...
    def build(self) -> JobFamilyTimeline: ...
