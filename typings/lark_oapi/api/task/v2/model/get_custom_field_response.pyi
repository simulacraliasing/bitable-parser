from .get_custom_field_response_body import GetCustomFieldResponseBody as GetCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetCustomFieldResponse(BaseResponse):
    data: GetCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
