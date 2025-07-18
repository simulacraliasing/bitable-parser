from .create_app_response_body import CreateAppResponseBody as CreateAppResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppResponse(BaseResponse):
    data: CreateAppResponseBody | None
    def __init__(self, d=None) -> None: ...
