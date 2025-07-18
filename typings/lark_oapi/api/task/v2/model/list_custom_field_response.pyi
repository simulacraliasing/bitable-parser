from .list_custom_field_response_body import ListCustomFieldResponseBody as ListCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListCustomFieldResponse(BaseResponse):
    data: ListCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
