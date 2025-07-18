from .upload_prepare_media_response_body import UploadPrepareMediaResponseBody as UploadPrepareMediaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadPrepareMediaResponse(BaseResponse):
    data: UploadPrepareMediaResponseBody | None
    def __init__(self, d=None) -> None: ...
