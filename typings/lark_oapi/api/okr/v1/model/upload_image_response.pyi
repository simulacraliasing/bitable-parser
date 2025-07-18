from .upload_image_response_body import UploadImageResponseBody as UploadImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UploadImageResponse(BaseResponse):
    data: UploadImageResponseBody | None
    def __init__(self, d=None) -> None: ...
