from .ask_app_knowledge_response_body import AskAppKnowledgeResponseBody as AskAppKnowledgeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AskAppKnowledgeResponse(BaseResponse):
    data: AskAppKnowledgeResponseBody | None
    def __init__(self, d=None) -> None: ...
