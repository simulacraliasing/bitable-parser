from ..model.create_leave_granting_record_request import CreateLeaveGrantingRecordRequest as CreateLeaveGrantingRecordRequest
from ..model.create_leave_granting_record_response import CreateLeaveGrantingRecordResponse as CreateLeaveGrantingRecordResponse
from ..model.delete_leave_granting_record_request import DeleteLeaveGrantingRecordRequest as DeleteLeaveGrantingRecordRequest
from ..model.delete_leave_granting_record_response import DeleteLeaveGrantingRecordResponse as DeleteLeaveGrantingRecordResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class LeaveGrantingRecord:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateLeaveGrantingRecordRequest, option: RequestOption | None = None) -> CreateLeaveGrantingRecordResponse: ...
    async def acreate(self, request: CreateLeaveGrantingRecordRequest, option: RequestOption | None = None) -> CreateLeaveGrantingRecordResponse: ...
    def delete(self, request: DeleteLeaveGrantingRecordRequest, option: RequestOption | None = None) -> DeleteLeaveGrantingRecordResponse: ...
    async def adelete(self, request: DeleteLeaveGrantingRecordRequest, option: RequestOption | None = None) -> DeleteLeaveGrantingRecordResponse: ...
