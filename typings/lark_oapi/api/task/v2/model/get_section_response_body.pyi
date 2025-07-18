from .section import Section as Section
from lark_oapi.core.construct import init as init

class GetSectionResponseBody:
    section: Section | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> GetSectionResponseBodyBuilder: ...

class GetSectionResponseBodyBuilder:
    def __init__(self) -> None: ...
    def section(self, section: Section) -> GetSectionResponseBodyBuilder: ...
    def build(self) -> GetSectionResponseBody: ...
