from .search_basic_info_bank_branch_response_body import SearchBasicInfoBankBranchResponseBody as SearchBasicInfoBankBranchResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchBasicInfoBankBranchResponse(BaseResponse):
    data: SearchBasicInfoBankBranchResponseBody | None
    def __init__(self, d=None) -> None: ...
