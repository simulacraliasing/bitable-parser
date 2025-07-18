from .create_file_comment_response_body import CreateFileCommentResponseBody as CreateFileCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateFileCommentResponse(BaseResponse):
    data: CreateFileCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
