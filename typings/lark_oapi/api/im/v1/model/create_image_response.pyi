from .create_image_response_body import CreateImageResponseBody as CreateImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateImageResponse(BaseResponse):
    data: CreateImageResponseBody | None
    def __init__(self, d=None) -> None: ...
