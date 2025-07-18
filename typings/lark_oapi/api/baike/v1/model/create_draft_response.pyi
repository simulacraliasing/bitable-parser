from .create_draft_response_body import CreateDraftResponseBody as CreateDraftResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateDraftResponse(BaseResponse):
    data: CreateDraftResponseBody | None
    def __init__(self, d=None) -> None: ...
