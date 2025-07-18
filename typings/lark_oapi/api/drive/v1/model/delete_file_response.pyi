from .delete_file_response_body import DeleteFileResponseBody as DeleteFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class DeleteFileResponse(BaseResponse):
    data: DeleteFileResponseBody | None
    def __init__(self, d=None) -> None: ...
