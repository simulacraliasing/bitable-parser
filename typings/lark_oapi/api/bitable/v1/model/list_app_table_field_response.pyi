from .list_app_table_field_response_body import ListAppTableFieldResponseBody as ListAppTableFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppTableFieldResponse(BaseResponse):
    data: ListAppTableFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
