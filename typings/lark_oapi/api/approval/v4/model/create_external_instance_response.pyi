from .create_external_instance_response_body import CreateExternalInstanceResponseBody as CreateExternalInstanceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateExternalInstanceResponse(BaseResponse):
    data: CreateExternalInstanceResponseBody | None
    def __init__(self, d=None) -> None: ...
