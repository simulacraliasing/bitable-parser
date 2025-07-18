from .doc_passage_param import DocPassageParam as DocPassageParam
from .helpdesk_passage_param import HelpdeskPassageParam as HelpdeskPassageParam
from .lingo_passage_param import LingoPassageParam as LingoPassageParam
from .message_passage_param import MessagePassageParam as MessagePassageParam
from .web_passage_param import WebPassageParam as WebPassageParam
from .wiki_passage_param import WikiPassageParam as WikiPassageParam
from lark_oapi.core.construct import init as init

class PassageParam:
    doc_param: DocPassageParam | None
    wiki_param: WikiPassageParam | None
    web_param: WebPassageParam | None
    helpdesk_param: HelpdeskPassageParam | None
    lingo_param: LingoPassageParam | None
    message_param: MessagePassageParam | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> PassageParamBuilder: ...

class PassageParamBuilder:
    def __init__(self) -> None: ...
    def doc_param(self, doc_param: DocPassageParam) -> PassageParamBuilder: ...
    def wiki_param(self, wiki_param: WikiPassageParam) -> PassageParamBuilder: ...
    def web_param(self, web_param: WebPassageParam) -> PassageParamBuilder: ...
    def helpdesk_param(self, helpdesk_param: HelpdeskPassageParam) -> PassageParamBuilder: ...
    def lingo_param(self, lingo_param: LingoPassageParam) -> PassageParamBuilder: ...
    def message_param(self, message_param: MessagePassageParam) -> PassageParamBuilder: ...
    def build(self) -> PassageParam: ...
