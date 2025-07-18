from .create_external_background_check_response_body import CreateExternalBackgroundCheckResponseBody as CreateExternalBackgroundCheckResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalBackgroundCheckResponse(BaseResponse):
    data: CreateExternalBackgroundCheckResponseBody | None
    def __init__(self, d=None) -> None: ...
