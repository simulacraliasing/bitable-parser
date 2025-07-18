from .get_application_app_version_response_body import GetApplicationAppVersionResponseBody as GetApplicationAppVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationAppVersionResponse(BaseResponse):
    data: GetApplicationAppVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
