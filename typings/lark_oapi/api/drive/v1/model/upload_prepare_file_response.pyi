from .upload_prepare_file_response_body import UploadPrepareFileResponseBody as UploadPrepareFileResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadPrepareFileResponse(BaseResponse):
    data: UploadPrepareFileResponseBody | None
    def __init__(self, d=None) -> None: ...
