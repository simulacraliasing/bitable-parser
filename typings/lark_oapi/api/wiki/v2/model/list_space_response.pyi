from .list_space_response_body import ListSpaceResponseBody as ListSpaceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSpaceResponse(BaseResponse):
    data: ListSpaceResponseBody | None
    def __init__(self, d=None) -> None: ...
