from lark_oapi.core.construct import init as init

class CreateExamRequestBody:
    application_id: str | None
    exam_resource_name: str | None
    score: float | None
    uuid: str | None
    operator_id: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> CreateExamRequestBodyBuilder: ...

class CreateExamRequestBodyBuilder:
    def __init__(self) -> None: ...
    def application_id(self, application_id: str) -> CreateExamRequestBodyBuilder: ...
    def exam_resource_name(self, exam_resource_name: str) -> CreateExamRequestBodyBuilder: ...
    def score(self, score: float) -> CreateExamRequestBodyBuilder: ...
    def uuid(self, uuid: str) -> CreateExamRequestBodyBuilder: ...
    def operator_id(self, operator_id: str) -> CreateExamRequestBodyBuilder: ...
    def build(self) -> CreateExamRequestBody: ...
