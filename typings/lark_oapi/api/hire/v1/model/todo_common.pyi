from lark_oapi.core.construct import init as init

class TodoCommon:
    talent_id: str | None
    job_id: str | None
    application_id: str | None
    id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> TodoCommonBuilder: ...

class TodoCommonBuilder:
    def __init__(self) -> None: ...
    def talent_id(self, talent_id: str) -> TodoCommonBuilder: ...
    def job_id(self, job_id: str) -> TodoCommonBuilder: ...
    def application_id(self, application_id: str) -> TodoCommonBuilder: ...
    def id(self, id: str) -> TodoCommonBuilder: ...
    def build(self) -> TodoCommon: ...
