from .create_app_table_field_response_body import CreateAppTableFieldResponseBody as CreateAppTableFieldResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateAppTableFieldResponse(BaseResponse):
    data: CreateAppTableFieldResponseBody | None
    def __init__(self, d=None) -> None: ...
