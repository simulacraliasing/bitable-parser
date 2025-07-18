from .delete_instance_comment_response_body import DeleteInstanceCommentResponseBody as DeleteInstanceCommentResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteInstanceCommentResponse(BaseResponse):
    data: DeleteInstanceCommentResponseBody | None
    def __init__(self, d=None) -> None: ...
