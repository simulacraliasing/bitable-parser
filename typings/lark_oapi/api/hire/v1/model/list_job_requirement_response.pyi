from .list_job_requirement_response_body import ListJobRequirementResponseBody as ListJobRequirementResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListJobRequirementResponse(BaseResponse):
    data: ListJobRequirementResponseBody | None
    def __init__(self, d=None) -> None: ...
