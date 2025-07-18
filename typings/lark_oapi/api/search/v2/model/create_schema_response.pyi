from .create_schema_response_body import CreateSchemaResponseBody as CreateSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSchemaResponse(BaseResponse):
    data: CreateSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
