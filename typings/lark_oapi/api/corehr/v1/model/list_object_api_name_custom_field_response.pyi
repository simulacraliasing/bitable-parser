from .list_object_api_name_custom_field_response_body import ListObjectApiNameCustomFieldResponseBody as ListObjectApiNameCustomFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListObjectApiNameCustomFieldResponse(BaseResponse):
    data: ListObjectApiNameCustomFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
