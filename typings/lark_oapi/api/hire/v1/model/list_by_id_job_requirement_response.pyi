from .list_by_id_job_requirement_response_body import ListByIdJobRequirementResponseBody as ListByIdJobRequirementResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListByIdJobRequirementResponse(BaseResponse):
    data: ListByIdJobRequirementResponseBody | None
    def __init__(self, d=None) -> None: ...
