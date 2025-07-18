from .search_talent_pool_response_body import SearchTalentPoolResponseBody as SearchTalentPoolResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchTalentPoolResponse(BaseResponse):
    data: SearchTalentPoolResponseBody | None
    def __init__(self, d=None) -> None: ...
