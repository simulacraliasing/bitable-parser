from .create_aily_session_aily_message_response_body import CreateAilySessionAilyMessageResponseBody as CreateAilySessionAilyMessageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAilySessionAilyMessageResponse(BaseResponse):
    data: CreateAilySessionAilyMessageResponseBody | None
    def __init__(self, d=None) -> None: ...
