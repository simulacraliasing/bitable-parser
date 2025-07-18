from .create_custom_field_option_response_body import CreateCustomFieldOptionResponseBody as CreateCustomFieldOptionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateCustomFieldOptionResponse(BaseResponse):
    data: CreateCustomFieldOptionResponseBody | None
    def __init__(self, d=None) -> None: ...
