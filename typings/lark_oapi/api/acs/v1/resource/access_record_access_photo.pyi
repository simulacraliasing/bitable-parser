from ..model.get_access_record_access_photo_request import GetAccessRecordAccessPhotoRequest as GetAccessRecordAccessPhotoRequest
from ..model.get_access_record_access_photo_response import GetAccessRecordAccessPhotoResponse as GetAccessRecordAccessPhotoResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AccessRecordAccessPhoto:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetAccessRecordAccessPhotoRequest, option: RequestOption | None = None) -> GetAccessRecordAccessPhotoResponse: ...
    async def aget(self, request: GetAccessRecordAccessPhotoRequest, option: RequestOption | None = None) -> GetAccessRecordAccessPhotoResponse: ...
