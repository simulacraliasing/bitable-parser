from .create_instance_comment_response_body import CreateInstanceCommentResponseBody as CreateInstanceCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateInstanceCommentResponse(BaseResponse):
    data: CreateInstanceCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
