from .update_external_application_response_body import UpdateExternalApplicationResponseBody as UpdateExternalApplicationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateExternalApplicationResponse(BaseResponse):
    data: UpdateExternalApplicationResponseBody | None
    def __init__(self, d=None) -> None: ...
