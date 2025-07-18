from lark_oapi.core.construct import init as init

class BatchGetJobLevelRequestBody:
    job_level_ids: list[str] | None
    job_level_codes: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> BatchGetJobLevelRequestBodyBuilder: ...

class BatchGetJobLevelRequestBodyBuilder:
    def __init__(self) -> None: ...
    def job_level_ids(self, job_level_ids: list[str]) -> BatchGetJobLevelRequestBodyBuilder: ...
    def job_level_codes(self, job_level_codes: list[str]) -> BatchGetJobLevelRequestBodyBuilder: ...
    def build(self) -> BatchGetJobLevelRequestBody: ...
