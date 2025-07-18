from .search_probation_response_body import SearchProbationResponseBody as SearchProbationResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchProbationResponse(BaseResponse):
    data: SearchProbationResponseBody | None
    def __init__(self, d=None) -> None: ...
