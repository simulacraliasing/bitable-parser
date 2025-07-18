from .get_spreadsheet_sheet_filter_view_condition_response_body import GetSpreadsheetSheetFilterViewConditionResponseBody as GetSpreadsheetSheetFilterViewConditionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    data: GetSpreadsheetSheetFilterViewConditionResponseBody | None
    def __init__(self, d=None) -> None: ...
