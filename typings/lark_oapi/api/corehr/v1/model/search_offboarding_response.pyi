from .search_offboarding_response_body import SearchOffboardingResponseBody as SearchOffboardingResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchOffboardingResponse(BaseResponse):
    data: SearchOffboardingResponseBody | None
    def __init__(self, d=None) -> None: ...
