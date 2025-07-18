from .add_enum_option_common_data_meta_data_response_body import AddEnumOptionCommonDataMetaDataResponseBody as AddEnumOptionCommonDataMetaDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class AddEnumOptionCommonDataMetaDataResponse(BaseResponse):
    data: AddEnumOptionCommonDataMetaDataResponseBody | None
    def __init__(self, d=None) -> None: ...
