from .get_space_response_body import GetSpaceResponseBody as GetSpaceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpaceResponse(BaseResponse):
    data: GetSpaceResponseBody | None
    def __init__(self, d=None) -> None: ...
