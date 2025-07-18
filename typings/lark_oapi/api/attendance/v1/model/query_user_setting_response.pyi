from .query_user_setting_response_body import QueryUserSettingResponseBody as QueryUserSettingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserSettingResponse(BaseResponse):
    data: QueryUserSettingResponseBody | None
    def __init__(self, d=None) -> None: ...
