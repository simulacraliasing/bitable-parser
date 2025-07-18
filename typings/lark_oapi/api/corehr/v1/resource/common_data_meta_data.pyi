from ..model.add_enum_option_common_data_meta_data_request import AddEnumOptionCommonDataMetaDataRequest as AddEnumOptionCommonDataMetaDataRequest
from ..model.add_enum_option_common_data_meta_data_response import AddEnumOptionCommonDataMetaDataResponse as AddEnumOptionCommonDataMetaDataResponse
from ..model.edit_enum_option_common_data_meta_data_request import EditEnumOptionCommonDataMetaDataRequest as EditEnumOptionCommonDataMetaDataRequest
from ..model.edit_enum_option_common_data_meta_data_response import EditEnumOptionCommonDataMetaDataResponse as EditEnumOptionCommonDataMetaDataResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class CommonDataMetaData:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def add_enum_option(self, request: AddEnumOptionCommonDataMetaDataRequest, option: RequestOption | None = None) -> AddEnumOptionCommonDataMetaDataResponse: ...
    async def aadd_enum_option(self, request: AddEnumOptionCommonDataMetaDataRequest, option: RequestOption | None = None) -> AddEnumOptionCommonDataMetaDataResponse: ...
    def edit_enum_option(self, request: EditEnumOptionCommonDataMetaDataRequest, option: RequestOption | None = None) -> EditEnumOptionCommonDataMetaDataResponse: ...
    async def aedit_enum_option(self, request: EditEnumOptionCommonDataMetaDataRequest, option: RequestOption | None = None) -> EditEnumOptionCommonDataMetaDataResponse: ...
