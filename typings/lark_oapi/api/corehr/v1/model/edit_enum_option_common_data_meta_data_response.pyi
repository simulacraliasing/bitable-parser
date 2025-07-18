from .edit_enum_option_common_data_meta_data_response_body import EditEnumOptionCommonDataMetaDataResponseBody as EditEnumOptionCommonDataMetaDataResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class EditEnumOptionCommonDataMetaDataResponse(BaseResponse):
    data: EditEnumOptionCommonDataMetaDataResponseBody | None
    def __init__(self, d=None) -> None: ...
