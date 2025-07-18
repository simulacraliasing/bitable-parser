from .upload_finish_file_response_body import UploadFinishFileResponseBody as UploadFinishFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadFinishFileResponse(BaseResponse):
    data: UploadFinishFileResponseBody | None
    def __init__(self, d=None) -> None: ...
