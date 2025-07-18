from .query_datasource_record_response_body import QueryDatasourceRecordResponseBody as QueryDatasourceRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QueryDatasourceRecordResponse(BaseResponse):
    data: QueryDatasourceRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
