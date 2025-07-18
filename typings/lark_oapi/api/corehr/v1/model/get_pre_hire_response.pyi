from .get_pre_hire_response_body import GetPreHireResponseBody as GetPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetPreHireResponse(BaseResponse):
    data: GetPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
