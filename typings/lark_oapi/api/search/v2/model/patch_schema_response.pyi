from .patch_schema_response_body import PatchSchemaResponseBody as PatchSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchSchemaResponse(BaseResponse):
    data: PatchSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
