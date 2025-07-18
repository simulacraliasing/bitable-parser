from ..model.create_image_request import CreateImageRequest as CreateImageRequest
from ..model.create_image_response import CreateImageResponse as CreateImageResponse
from ..model.get_image_request import GetImageRequest as GetImageRequest
from ..model.get_image_response import GetImageResponse as GetImageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class Image:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateImageRequest, option: RequestOption | None = None) -> CreateImageResponse: ...
    async def acreate(self, request: CreateImageRequest, option: RequestOption | None = None) -> CreateImageResponse: ...
    def get(self, request: GetImageRequest, option: RequestOption | None = None) -> GetImageResponse: ...
    async def aget(self, request: GetImageRequest, option: RequestOption | None = None) -> GetImageResponse: ...
