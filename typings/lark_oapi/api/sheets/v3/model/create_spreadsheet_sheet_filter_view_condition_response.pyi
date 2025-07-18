from .create_spreadsheet_sheet_filter_view_condition_response_body import CreateSpreadsheetSheetFilterViewConditionResponseBody as CreateSpreadsheetSheetFilterViewConditionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    data: CreateSpreadsheetSheetFilterViewConditionResponseBody | None
    def __init__(self, d=None) -> None: ...
