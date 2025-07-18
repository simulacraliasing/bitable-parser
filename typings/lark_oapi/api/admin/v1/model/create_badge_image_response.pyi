from .create_badge_image_response_body import CreateBadgeImageResponseBody as CreateBadgeImageResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateBadgeImageResponse(BaseResponse):
    data: CreateBadgeImageResponseBody | None
    def __init__(self, d=None) -> None: ...
