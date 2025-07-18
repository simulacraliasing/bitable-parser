from .get_note_response_body import GetNoteResponseBody as GetNoteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetNoteResponse(BaseResponse):
    data: GetNoteResponseBody | None
    def __init__(self, d=None) -> None: ...
