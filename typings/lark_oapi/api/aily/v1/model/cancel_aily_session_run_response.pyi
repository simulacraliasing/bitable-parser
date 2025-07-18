from .cancel_aily_session_run_response_body import CancelAilySessionRunResponseBody as CancelAilySessionRunResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CancelAilySessionRunResponse(BaseResponse):
    data: CancelAilySessionRunResponseBody | None
    def __init__(self, d=None) -> None: ...
