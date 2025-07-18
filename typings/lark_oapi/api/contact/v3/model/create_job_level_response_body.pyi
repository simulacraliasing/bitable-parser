from .job_level import JobLevel as JobLevel
from lark_oapi.core.construct import init as init

class CreateJobLevelResponseBody:
    job_level: JobLevel | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateJobLevelResponseBodyBuilder: ...

class CreateJobLevelResponseBodyBuilder:
    def __init__(self) -> None: ...
    def job_level(self, job_level: JobLevel) -> CreateJobLevelResponseBodyBuilder: ...
    def build(self) -> CreateJobLevelResponseBody: ...
