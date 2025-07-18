from .update_app_response_body import UpdateAppResponseBody as UpdateAppResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAppResponse(BaseResponse):
    data: UpdateAppResponseBody | None
    def __init__(self, d=None) -> None: ...
