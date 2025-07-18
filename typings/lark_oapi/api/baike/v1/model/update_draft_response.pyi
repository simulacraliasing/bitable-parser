from .update_draft_response_body import UpdateDraftResponseBody as UpdateDraftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateDraftResponse(BaseResponse):
    data: UpdateDraftResponseBody | None
    def __init__(self, d=None) -> None: ...
