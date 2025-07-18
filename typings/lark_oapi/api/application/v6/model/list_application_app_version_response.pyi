from .list_application_app_version_response_body import ListApplicationAppVersionResponseBody as ListApplicationAppVersionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListApplicationAppVersionResponse(BaseResponse):
    data: ListApplicationAppVersionResponseBody | None
    def __init__(self, d=None) -> None: ...
