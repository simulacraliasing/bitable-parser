from .create_note_response_body import CreateNoteResponseBody as CreateNoteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateNoteResponse(BaseResponse):
    data: CreateNoteResponseBody | None
    def __init__(self, d=None) -> None: ...
