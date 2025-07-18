from .remove_instance_comment_response_body import RemoveInstanceCommentResponseBody as RemoveInstanceCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class RemoveInstanceCommentResponse(BaseResponse):
    data: RemoveInstanceCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
