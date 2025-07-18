from .list_external_application_response_body import ListExternalApplicationResponseBody as ListExternalApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListExternalApplicationResponse(BaseResponse):
    data: ListExternalApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
