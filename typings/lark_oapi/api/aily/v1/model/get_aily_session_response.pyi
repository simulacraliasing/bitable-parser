from .get_aily_session_response_body import GetAilySessionResponseBody as GetAilySessionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAilySessionResponse(BaseResponse):
    data: GetAilySessionResponseBody | None
    def __init__(self, d=None) -> None: ...
