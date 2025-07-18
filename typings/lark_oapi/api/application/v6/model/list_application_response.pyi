from .list_application_response_body import ListApplicationResponseBody as ListApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListApplicationResponse(BaseResponse):
    data: ListApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
