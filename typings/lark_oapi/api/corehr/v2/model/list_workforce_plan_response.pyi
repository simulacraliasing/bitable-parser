from .list_workforce_plan_response_body import ListWorkforcePlanResponseBody as ListWorkforcePlanResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListWorkforcePlanResponse(BaseResponse):
    data: ListWorkforcePlanResponseBody | None
    def __init__(self, d=None) -> None: ...
