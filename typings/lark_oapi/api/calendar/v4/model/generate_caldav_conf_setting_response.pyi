from .generate_caldav_conf_setting_response_body import GenerateCaldavConfSettingResponseBody as GenerateCaldavConfSettingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GenerateCaldavConfSettingResponse(BaseResponse):
    data: GenerateCaldavConfSettingResponseBody | None
    def __init__(self, d=None) -> None: ...
