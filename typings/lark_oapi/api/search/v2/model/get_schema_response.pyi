from .get_schema_response_body import GetSchemaResponseBody as GetSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSchemaResponse(BaseResponse):
    data: GetSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
