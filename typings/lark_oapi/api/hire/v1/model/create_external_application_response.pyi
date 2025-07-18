from .create_external_application_response_body import CreateExternalApplicationResponseBody as CreateExternalApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalApplicationResponse(BaseResponse):
    data: CreateExternalApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
