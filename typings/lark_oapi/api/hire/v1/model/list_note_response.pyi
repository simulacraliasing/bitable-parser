from .list_note_response_body import ListNoteResponseBody as ListNoteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListNoteResponse(BaseResponse):
    data: ListNoteResponseBody | None
    def __init__(self, d=None) -> None: ...
