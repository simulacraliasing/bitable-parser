from ..model.convert_common_data_id_request import ConvertCommonDataIdRequest as ConvertCommonDataIdRequest
from ..model.convert_common_data_id_response import ConvertCommonDataIdResponse as ConvertCommonDataIdResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CommonDataId:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def convert(self, request: ConvertCommonDataIdRequest, option: RequestOption | None = None) -> ConvertCommonDataIdResponse: ...
    async def aconvert(self, request: ConvertCommonDataIdRequest, option: RequestOption | None = None) -> ConvertCommonDataIdResponse: ...
