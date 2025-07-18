from .basic_recognize_image_response_body import BasicRecognizeImageResponseBody as BasicRecognizeImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BasicRecognizeImageResponse(BaseResponse):
    data: BasicRecognizeImageResponseBody | None
    def __init__(self, d=None) -> None: ...
