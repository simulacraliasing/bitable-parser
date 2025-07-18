from ..model.create_spreadsheet_sheet_filter_view_request import CreateSpreadsheetSheetFilterViewRequest as CreateSpreadsheetSheetFilterViewRequest
from ..model.create_spreadsheet_sheet_filter_view_response import CreateSpreadsheetSheetFilterViewResponse as CreateSpreadsheetSheetFilterViewResponse
from ..model.delete_spreadsheet_sheet_filter_view_request import DeleteSpreadsheetSheetFilterViewRequest as DeleteSpreadsheetSheetFilterViewRequest
from ..model.delete_spreadsheet_sheet_filter_view_response import DeleteSpreadsheetSheetFilterViewResponse as DeleteSpreadsheetSheetFilterViewResponse
from ..model.get_spreadsheet_sheet_filter_view_request import GetSpreadsheetSheetFilterViewRequest as GetSpreadsheetSheetFilterViewRequest
from ..model.get_spreadsheet_sheet_filter_view_response import GetSpreadsheetSheetFilterViewResponse as GetSpreadsheetSheetFilterViewResponse
from ..model.patch_spreadsheet_sheet_filter_view_request import PatchSpreadsheetSheetFilterViewRequest as PatchSpreadsheetSheetFilterViewRequest
from ..model.patch_spreadsheet_sheet_filter_view_response import PatchSpreadsheetSheetFilterViewResponse as PatchSpreadsheetSheetFilterViewResponse
from ..model.query_spreadsheet_sheet_filter_view_request import QuerySpreadsheetSheetFilterViewRequest as QuerySpreadsheetSheetFilterViewRequest
from ..model.query_spreadsheet_sheet_filter_view_response import QuerySpreadsheetSheetFilterViewResponse as QuerySpreadsheetSheetFilterViewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class SpreadsheetSheetFilterView:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> CreateSpreadsheetSheetFilterViewResponse: ...
    async def acreate(self, request: CreateSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> CreateSpreadsheetSheetFilterViewResponse: ...
    def delete(self, request: DeleteSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> DeleteSpreadsheetSheetFilterViewResponse: ...
    async def adelete(self, request: DeleteSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> DeleteSpreadsheetSheetFilterViewResponse: ...
    def get(self, request: GetSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> GetSpreadsheetSheetFilterViewResponse: ...
    async def aget(self, request: GetSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> GetSpreadsheetSheetFilterViewResponse: ...
    def patch(self, request: PatchSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> PatchSpreadsheetSheetFilterViewResponse: ...
    async def apatch(self, request: PatchSpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> PatchSpreadsheetSheetFilterViewResponse: ...
    def query(self, request: QuerySpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> QuerySpreadsheetSheetFilterViewResponse: ...
    async def aquery(self, request: QuerySpreadsheetSheetFilterViewRequest, option: RequestOption | None = None) -> QuerySpreadsheetSheetFilterViewResponse: ...
