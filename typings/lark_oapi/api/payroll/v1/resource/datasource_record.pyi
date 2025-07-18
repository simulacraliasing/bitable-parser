from ..model.query_datasource_record_request import QueryDatasourceRecordRequest as QueryDatasourceRecordRequest
from ..model.query_datasource_record_response import QueryDatasourceRecordResponse as QueryDatasourceRecordResponse
from ..model.save_datasource_record_request import SaveDatasourceRecordRequest as SaveDatasourceRecordRequest
from ..model.save_datasource_record_response import SaveDatasourceRecordResponse as SaveDatasourceRecordResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class DatasourceRecord:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def query(self, request: QueryDatasourceRecordRequest, option: RequestOption | None = None) -> QueryDatasourceRecordResponse: ...
    async def aquery(self, request: QueryDatasourceRecordRequest, option: RequestOption | None = None) -> QueryDatasourceRecordResponse: ...
    def save(self, request: SaveDatasourceRecordRequest, option: RequestOption | None = None) -> SaveDatasourceRecordResponse: ...
    async def asave(self, request: SaveDatasourceRecordRequest, option: RequestOption | None = None) -> SaveDatasourceRecordResponse: ...
