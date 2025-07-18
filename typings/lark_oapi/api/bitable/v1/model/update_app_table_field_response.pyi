from .update_app_table_field_response_body import UpdateAppTableFieldResponseBody as UpdateAppTableFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateAppTableFieldResponse(BaseResponse):
    data: UpdateAppTableFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
