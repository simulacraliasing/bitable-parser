from .create_space_node_response_body import CreateSpaceNodeResponseBody as CreateSpaceNodeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpaceNodeResponse(BaseResponse):
    data: CreateSpaceNodeResponseBody | None
    def __init__(self, d=None) -> None: ...
