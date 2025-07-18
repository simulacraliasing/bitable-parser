from .equation import Equation as Equation
from .inline_block import InlineBlock as InlineBlock
from .inline_file import InlineFile as InlineFile
from .mention_doc import MentionDoc as MentionDoc
from .mention_user import MentionUser as MentionUser
from .reminder import Reminder as Reminder
from .text_run import TextRun as TextRun
from .undefined_element import UndefinedElement as UndefinedElement
from lark_oapi.core.construct import init as init

class AgendaTitleElement:
    text_run: TextRun | None
    mention_user: MentionUser | None
    mention_doc: MentionDoc | None
    reminder: Reminder | None
    file: InlineFile | None
    undefined: UndefinedElement | None
    inline_block: InlineBlock | None
    equation: Equation | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> AgendaTitleElementBuilder: ...

class AgendaTitleElementBuilder:
    def __init__(self) -> None: ...
    def text_run(self, text_run: TextRun) -> AgendaTitleElementBuilder: ...
    def mention_user(self, mention_user: MentionUser) -> AgendaTitleElementBuilder: ...
    def mention_doc(self, mention_doc: MentionDoc) -> AgendaTitleElementBuilder: ...
    def reminder(self, reminder: Reminder) -> AgendaTitleElementBuilder: ...
    def file(self, file: InlineFile) -> AgendaTitleElementBuilder: ...
    def undefined(self, undefined: UndefinedElement) -> AgendaTitleElementBuilder: ...
    def inline_block(self, inline_block: InlineBlock) -> AgendaTitleElementBuilder: ...
    def equation(self, equation: Equation) -> AgendaTitleElementBuilder: ...
    def build(self) -> AgendaTitleElement: ...
