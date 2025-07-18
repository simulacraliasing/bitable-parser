from .create_app_table_response_body import CreateAppTableResponseBody as CreateAppTableResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppTableResponse(BaseResponse):
    data: CreateAppTableResponseBody | None
    def __init__(self, d=None) -> None: ...
