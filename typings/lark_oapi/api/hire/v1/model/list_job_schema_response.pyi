from .list_job_schema_response_body import ListJobSchemaResponseBody as ListJobSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobSchemaResponse(BaseResponse):
    data: ListJobSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
