from ..model.upload_image_request import UploadImageRequest as UploadImageRequest
from ..model.upload_image_response import UploadImageResponse as UploadImageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class Image:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def upload(self, request: UploadImageRequest, option: RequestOption | None = None) -> UploadImageResponse: ...
    async def aupload(self, request: UploadImageRequest, option: RequestOption | None = None) -> UploadImageResponse: ...
