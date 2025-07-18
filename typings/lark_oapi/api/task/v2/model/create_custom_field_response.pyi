from .create_custom_field_response_body import CreateCustomFieldResponseBody as CreateCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCustomFieldResponse(BaseResponse):
    data: CreateCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
