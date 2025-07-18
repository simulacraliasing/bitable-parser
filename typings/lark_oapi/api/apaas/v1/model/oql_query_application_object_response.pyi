from .oql_query_application_object_response_body import OqlQueryApplicationObjectResponseBody as OqlQueryApplicationObjectResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class OqlQueryApplicationObjectResponse(BaseResponse):
    data: OqlQueryApplicationObjectResponseBody | None
    def __init__(self, d=None) -> None: ...
