from .update_space_setting_response_body import UpdateSpaceSettingResponseBody as UpdateSpaceSettingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateSpaceSettingResponse(BaseResponse):
    data: UpdateSpaceSettingResponseBody | None
    def __init__(self, d=None) -> None: ...
