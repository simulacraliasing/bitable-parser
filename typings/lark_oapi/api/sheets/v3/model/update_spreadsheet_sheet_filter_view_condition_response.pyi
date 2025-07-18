from .update_spreadsheet_sheet_filter_view_condition_response_body import UpdateSpreadsheetSheetFilterViewConditionResponseBody as UpdateSpreadsheetSheetFilterViewConditionResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class UpdateSpreadsheetSheetFilterViewConditionResponse(BaseResponse):
    data: UpdateSpreadsheetSheetFilterViewConditionResponseBody | None
    def __init__(self, d=None) -> None: ...
