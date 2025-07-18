from .list_aily_session_run_response_body import ListAilySessionRunResponseBody as ListAilySessionRunResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAilySessionRunResponse(BaseResponse):
    data: ListAilySessionRunResponseBody | None
    def __init__(self, d=None) -> None: ...
