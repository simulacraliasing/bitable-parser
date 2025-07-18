from .upload_attachment_response_body import UploadAttachmentResponseBody as UploadAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadAttachmentResponse(BaseResponse):
    data: UploadAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
