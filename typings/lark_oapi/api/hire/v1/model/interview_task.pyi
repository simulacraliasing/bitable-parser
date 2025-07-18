from lark_oapi.core.construct import init as init

class InterviewTask:
    id: str | None
    job_id: str | None
    talent_id: str | None
    application_id: str | None
    activity_status: int | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> InterviewTaskBuilder: ...

class InterviewTaskBuilder:
    def __init__(self) -> None: ...
    def id(self, id: str) -> InterviewTaskBuilder: ...
    def job_id(self, job_id: str) -> InterviewTaskBuilder: ...
    def talent_id(self, talent_id: str) -> InterviewTaskBuilder: ...
    def application_id(self, application_id: str) -> InterviewTaskBuilder: ...
    def activity_status(self, activity_status: int) -> InterviewTaskBuilder: ...
    def build(self) -> InterviewTask: ...
