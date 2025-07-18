from .list_subdivision_response_body import ListSubdivisionResponseBody as ListSubdivisionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListSubdivisionResponse(BaseResponse):
    data: ListSubdivisionResponseBody | None
    def __init__(self, d=None) -> None: ...
