from .list_attachment_response_body import ListAttachmentResponseBody as ListAttachmentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAttachmentResponse(BaseResponse):
    data: ListAttachmentResponseBody | None
    def __init__(self, d=None) -> None: ...
