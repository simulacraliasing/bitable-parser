from .search_assigned_user_response_body import SearchAssignedUserResponseBody as SearchAssignedUserResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SearchAssignedUserResponse(BaseResponse):
    data: SearchAssignedUserResponseBody | None
    def __init__(self, d=None) -> None: ...
