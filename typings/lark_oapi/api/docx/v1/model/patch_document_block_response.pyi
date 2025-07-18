from .patch_document_block_response_body import PatchDocumentBlockResponseBody as PatchDocumentBlockResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchDocumentBlockResponse(BaseResponse):
    data: PatchDocumentBlockResponseBody | None
    def __init__(self, d=None) -> None: ...
