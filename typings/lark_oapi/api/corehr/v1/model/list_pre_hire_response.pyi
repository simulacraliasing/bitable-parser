from .list_pre_hire_response_body import ListPreHireResponseBody as ListPreHireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPreHireResponse(BaseResponse):
    data: ListPreHireResponseBody | None
    def __init__(self, d=None) -> None: ...
