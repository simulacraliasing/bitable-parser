from .upload_finish_media_response_body import UploadFinishMediaResponseBody as UploadFinishMediaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadFinishMediaResponse(BaseResponse):
    data: UploadFinishMediaResponseBody | None
    def __init__(self, d=None) -> None: ...
