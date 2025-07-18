from .list_repo_response_body import ListRepoResponseBody as ListRepoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListRepoResponse(BaseResponse):
    data: ListRepoResponseBody | None
    def __init__(self, d=None) -> None: ...
