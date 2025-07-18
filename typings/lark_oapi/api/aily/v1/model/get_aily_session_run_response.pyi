from .get_aily_session_run_response_body import GetAilySessionRunResponseBody as GetAilySessionRunResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAilySessionRunResponse(BaseResponse):
    data: GetAilySessionRunResponseBody | None
    def __init__(self, d=None) -> None: ...
