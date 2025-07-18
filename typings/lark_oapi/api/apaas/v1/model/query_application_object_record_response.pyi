from .query_application_object_record_response_body import QueryApplicationObjectRecordResponseBody as QueryApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryApplicationObjectRecordResponse(BaseResponse):
    data: QueryApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
