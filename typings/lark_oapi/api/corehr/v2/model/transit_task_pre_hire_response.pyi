from .transit_task_pre_hire_response_body import TransitTaskPreHireResponseBody as TransitTaskPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class TransitTaskPreHireResponse(BaseResponse):
    data: TransitTaskPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
