from .create_comment_response_body import CreateCommentResponseBody as CreateCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCommentResponse(BaseResponse):
    data: CreateCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
