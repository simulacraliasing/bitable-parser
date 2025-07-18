from ..model.basic_recognize_image_request import BasicRecognizeImageRequest as BasicRecognizeImageRequest
from ..model.basic_recognize_image_response import BasicRecognizeImageResponse as BasicRecognizeImageResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Image:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def basic_recognize(self, request: BasicRecognizeImageRequest, option: RequestOption | None = None) -> BasicRecognizeImageResponse: ...
    async def abasic_recognize(self, request: BasicRecognizeImageRequest, option: RequestOption | None = None) -> BasicRecognizeImageResponse: ...
