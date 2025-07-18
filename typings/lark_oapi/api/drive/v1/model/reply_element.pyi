from .docs_link import DocsLink as DocsLink
from .person import Person as Person
from .text_run import TextRun as TextRun
from lark_oapi.core.construct import init as init

class ReplyElement:
    type: str | None
    text_run: TextRun | None
    docs_link: DocsLink | None
    person: Person | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> ReplyElementBuilder: ...

class ReplyElementBuilder:
    def __init__(self) -> None: ...
    def type(self, type: str) -> ReplyElementBuilder: ...
    def text_run(self, text_run: TextRun) -> ReplyElementBuilder: ...
    def docs_link(self, docs_link: DocsLink) -> ReplyElementBuilder: ...
    def person(self, person: Person) -> ReplyElementBuilder: ...
    def build(self) -> ReplyElement: ...
