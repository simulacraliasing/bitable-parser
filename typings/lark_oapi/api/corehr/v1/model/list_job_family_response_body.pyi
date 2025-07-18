from .job_family import JobFamily as JobFamily
from lark_oapi.core.construct import init as init

class ListJobFamilyResponseBody:
    items: list[JobFamily] | None
    has_more: bool | None
    page_token: str | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ListJobFamilyResponseBodyBuilder: ...

class ListJobFamilyResponseBodyBuilder:
    def __init__(self) -> None: ...
    def items(self, items: list[JobFamily]) -> ListJobFamilyResponseBodyBuilder: ...
    def has_more(self, has_more: bool) -> ListJobFamilyResponseBodyBuilder: ...
    def page_token(self, page_token: str) -> ListJobFamilyResponseBodyBuilder: ...
    def build(self) -> ListJobFamilyResponseBody: ...
