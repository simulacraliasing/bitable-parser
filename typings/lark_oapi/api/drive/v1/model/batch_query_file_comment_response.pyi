from .batch_query_file_comment_response_body import BatchQueryFileCommentResponseBody as BatchQueryFileCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchQueryFileCommentResponse(BaseResponse):
    data: BatchQueryFileCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
