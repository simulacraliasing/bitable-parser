from .upload_all_file_response_body import UploadAllFileResponseBody as UploadAllFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadAllFileResponse(BaseResponse):
    data: UploadAllFileResponseBody | None
    def __init__(self, d=None) -> None: ...
