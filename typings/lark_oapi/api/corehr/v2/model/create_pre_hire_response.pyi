from .create_pre_hire_response_body import CreatePreHireResponseBody as CreatePreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreatePreHireResponse(BaseResponse):
    data: CreatePreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
