from .preview_attachment_response_body import PreviewAttachmentResponseBody as PreviewAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PreviewAttachmentResponse(BaseResponse):
    data: PreviewAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
