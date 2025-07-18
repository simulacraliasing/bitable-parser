from .update_external_background_check_response_body import UpdateExternalBackgroundCheckResponseBody as UpdateExternalBackgroundCheckResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateExternalBackgroundCheckResponse(BaseResponse):
    data: UpdateExternalBackgroundCheckResponseBody | None
    def __init__(self, d=None) -> None: ...
