from .get_application_response_body import GetApplicationResponseBody as GetApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationResponse(BaseResponse):
    data: GetApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
