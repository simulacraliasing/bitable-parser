from .save_datasource_record_response_body import SaveDatasourceRecordResponseBody as SaveDatasourceRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class SaveDatasourceRecordResponse(BaseResponse):
    data: SaveDatasourceRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
