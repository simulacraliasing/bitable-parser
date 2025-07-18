from ..model.create_badge_image_request import CreateBadgeImageRequest as CreateBadgeImageRequest
from ..model.create_badge_image_response import CreateBadgeImageResponse as CreateBadgeImageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class BadgeImage:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateBadgeImageRequest, option: RequestOption | None = None) -> CreateBadgeImageResponse: ...
    async def acreate(self, request: CreateBadgeImageRequest, option: RequestOption | None = None) -> CreateBadgeImageResponse: ...
