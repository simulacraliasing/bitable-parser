from .get_by_param_authorization_response_body import GetByParamAuthorizationResponseBody as GetByParamAuthorizationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetByParamAuthorizationResponse(BaseResponse):
    data: GetByParamAuthorizationResponseBody | None
    def __init__(self, d=None) -> None: ...
