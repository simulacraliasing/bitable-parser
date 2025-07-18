from lark_oapi.core.construct import init as init

class CreateJobGradeResponseBody:
    grade_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateJobGradeResponseBodyBuilder: ...

class CreateJobGradeResponseBodyBuilder:
    def __init__(self) -> None: ...
    def grade_id(self, grade_id: str) -> CreateJobGradeResponseBodyBuilder: ...
    def build(self) -> CreateJobGradeResponseBody: ...
