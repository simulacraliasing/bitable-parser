from .update_aily_session_response_body import UpdateAilySessionResponseBody as UpdateAilySessionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAilySessionResponse(BaseResponse):
    data: UpdateAilySessionResponseBody | None
    def __init__(self, d=None) -> None: ...
