from .list_app_table_form_field_response_body import ListAppTableFormFieldResponseBody as ListAppTableFormFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppTableFormFieldResponse(BaseResponse):
    data: ListAppTableFormFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
