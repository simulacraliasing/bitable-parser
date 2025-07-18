from .query_offboarding_response_body import QueryOffboardingResponseBody as QueryOffboardingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryOffboardingResponse(BaseResponse):
    data: QueryOffboardingResponseBody | None
    def __init__(self, d=None) -> None: ...
