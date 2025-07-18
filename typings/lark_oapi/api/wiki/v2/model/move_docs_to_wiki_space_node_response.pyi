from .move_docs_to_wiki_space_node_response_body import MoveDocsToWikiSpaceNodeResponseBody as MoveDocsToWikiSpaceNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MoveDocsToWikiSpaceNodeResponse(BaseResponse):
    data: MoveDocsToWikiSpaceNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
