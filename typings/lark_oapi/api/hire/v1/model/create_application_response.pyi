from .create_application_response_body import CreateApplicationResponseBody as CreateApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateApplicationResponse(BaseResponse):
    data: CreateApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
