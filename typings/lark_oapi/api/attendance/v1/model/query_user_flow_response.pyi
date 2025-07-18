from .query_user_flow_response_body import QueryUserFlowResponseBody as QueryUserFlowResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryUserFlowResponse(BaseResponse):
    data: QueryUserFlowResponseBody | None
    def __init__(self, d=None) -> None: ...
