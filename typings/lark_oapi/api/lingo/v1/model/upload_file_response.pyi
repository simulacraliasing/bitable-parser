from .upload_file_response_body import UploadFileResponseBody as UploadFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadFileResponse(BaseResponse):
    data: UploadFileResponseBody | None
    def __init__(self, d=None) -> None: ...
