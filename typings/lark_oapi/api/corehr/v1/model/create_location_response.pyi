from .create_location_response_body import CreateLocationResponseBody as CreateLocationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateLocationResponse(BaseResponse):
    data: CreateLocationResponseBody | None
    def __init__(self, d=None) -> None: ...
