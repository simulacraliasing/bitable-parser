from .create_aily_session_run_response_body import CreateAilySessionRunResponseBody as CreateAilySessionRunResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAilySessionRunResponse(BaseResponse):
    data: CreateAilySessionRunResponseBody | None
    def __init__(self, d=None) -> None: ...
