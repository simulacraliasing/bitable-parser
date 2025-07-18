from .knowledge_source_wiki_filter import KnowledgeSourceWikiFilter as KnowledgeSourceWikiFilter
from .knowledge_source_wiki_reject import KnowledgeSourceWikiReject as KnowledgeSourceWikiReject
from lark_oapi.core.construct import init as init

class EnterpriseKnowledgeSourceWikiParam:
    searchable: bool | None
    filter: KnowledgeSourceWikiFilter | None
    reject: KnowledgeSourceWikiReject | None
    def __init__(self, d=None) -> None: ...
    @staticmethod
    def builder() -> EnterpriseKnowledgeSourceWikiParamBuilder: ...

class EnterpriseKnowledgeSourceWikiParamBuilder:
    def __init__(self) -> None: ...
    def searchable(self, searchable: bool) -> EnterpriseKnowledgeSourceWikiParamBuilder: ...
    def filter(self, filter: KnowledgeSourceWikiFilter) -> EnterpriseKnowledgeSourceWikiParamBuilder: ...
    def reject(self, reject: KnowledgeSourceWikiReject) -> EnterpriseKnowledgeSourceWikiParamBuilder: ...
    def build(self) -> EnterpriseKnowledgeSourceWikiParam: ...
