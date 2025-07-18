from .patch_note_response_body import PatchNoteResponseBody as PatchNoteResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchNoteResponse(BaseResponse):
    data: PatchNoteResponseBody | None
    def __init__(self, d=None) -> None: ...
