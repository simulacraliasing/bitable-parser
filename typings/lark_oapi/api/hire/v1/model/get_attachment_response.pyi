from .get_attachment_response_body import GetAttachmentResponseBody as GetAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAttachmentResponse(BaseResponse):
    data: GetAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
