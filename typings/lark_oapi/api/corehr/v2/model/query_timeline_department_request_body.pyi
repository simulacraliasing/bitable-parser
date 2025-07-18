from lark_oapi.core.construct import init as init

class QueryTimelineDepartmentRequestBody:
    department_ids: list[str] | None
    effective_date: str | None
    fields: list[str] | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> QueryTimelineDepartmentRequestBodyBuilder: ...

class QueryTimelineDepartmentRequestBodyBuilder:
    def __init__(self) -> None: ...
    def department_ids(self, department_ids: list[str]) -> QueryTimelineDepartmentRequestBodyBuilder: ...
    def effective_date(self, effective_date: str) -> QueryTimelineDepartmentRequestBodyBuilder: ...
    def fields(self, fields: list[str]) -> QueryTimelineDepartmentRequestBodyBuilder: ...
    def build(self) -> QueryTimelineDepartmentRequestBody: ...
