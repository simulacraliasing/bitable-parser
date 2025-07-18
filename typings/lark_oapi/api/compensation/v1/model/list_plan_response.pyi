from .list_plan_response_body import ListPlanResponseBody as ListPlanResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListPlanResponse(BaseResponse):
    data: ListPlanResponseBody | None
    def __init__(self, d=None) -> None: ...
