from .search_diversity_inclusion_response_body import SearchDiversityInclusionResponseBody as SearchDiversityInclusionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchDiversityInclusionResponse(BaseResponse):
    data: SearchDiversityInclusionResponseBody | None
    def __init__(self, d=None) -> None: ...
