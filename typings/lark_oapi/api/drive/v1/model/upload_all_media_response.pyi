from .upload_all_media_response_body import UploadAllMediaResponseBody as UploadAllMediaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadAllMediaResponse(BaseResponse):
    data: UploadAllMediaResponseBody | None
    def __init__(self, d=None) -> None: ...
