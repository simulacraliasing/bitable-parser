from .create_aily_session_response_body import CreateAilySessionResponseBody as CreateAilySessionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAilySessionResponse(BaseResponse):
    data: CreateAilySessionResponseBody | None
    def __init__(self, d=None) -> None: ...
