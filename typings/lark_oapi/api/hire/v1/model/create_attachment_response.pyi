from .create_attachment_response_body import CreateAttachmentResponseBody as CreateAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAttachmentResponse(BaseResponse):
    data: CreateAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
