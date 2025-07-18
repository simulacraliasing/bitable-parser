from .modify_user_setting_response_body import ModifyUserSettingResponseBody as ModifyUserSettingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ModifyUserSettingResponse(BaseResponse):
    data: ModifyUserSettingResponseBody | None
    def __init__(self, d=None) -> None: ...
