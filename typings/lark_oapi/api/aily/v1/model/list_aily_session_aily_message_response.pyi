from .list_aily_session_aily_message_response_body import ListAilySessionAilyMessageResponseBody as ListAilySessionAilyMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAilySessionAilyMessageResponse(BaseResponse):
    data: ListAilySessionAilyMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
