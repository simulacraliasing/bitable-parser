from .get_aily_session_aily_message_response_body import GetAilySessionAilyMessageResponseBody as GetAilySessionAilyMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAilySessionAilyMessageResponse(BaseResponse):
    data: GetAilySessionAilyMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
