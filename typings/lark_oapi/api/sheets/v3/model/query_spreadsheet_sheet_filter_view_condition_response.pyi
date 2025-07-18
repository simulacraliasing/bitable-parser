from .query_spreadsheet_sheet_filter_view_condition_response_body import QuerySpreadsheetSheetFilterViewConditionResponseBody as QuerySpreadsheetSheetFilterViewConditionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class QuerySpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    data: QuerySpreadsheetSheetFilterViewConditionResponseBody | None
    def __init__(self, d=None) -> None: ...
