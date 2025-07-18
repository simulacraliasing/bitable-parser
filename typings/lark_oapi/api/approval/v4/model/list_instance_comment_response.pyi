from .list_instance_comment_response_body import ListInstanceCommentResponseBody as ListInstanceCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListInstanceCommentResponse(BaseResponse):
    data: ListInstanceCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
