from .get_scope_config_response_body import GetScopeConfigResponseBody as GetScopeConfigResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetScopeConfigResponse(BaseResponse):
    data: GetScopeConfigResponseBody | None
    def __init__(self, d=None) -> None: ...
