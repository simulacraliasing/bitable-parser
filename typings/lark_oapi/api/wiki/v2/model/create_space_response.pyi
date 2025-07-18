from .create_space_response_body import CreateSpaceResponseBody as CreateSpaceResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpaceResponse(BaseResponse):
    data: CreateSpaceResponseBody | None
    def __init__(self, d=None) -> None: ...
