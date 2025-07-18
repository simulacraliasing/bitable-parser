from .list_job_requirement_schema_response_body import ListJobRequirementSchemaResponseBody as ListJobRequirementSchemaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobRequirementSchemaResponse(BaseResponse):
    data: ListJobRequirementSchemaResponseBody | None
    def __init__(self, d=None) -> None: ...
