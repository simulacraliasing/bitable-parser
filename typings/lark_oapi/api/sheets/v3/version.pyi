from .resource import *

class V3:
    spreadsheet: Spreadsheet
    spreadsheet_sheet: SpreadsheetSheet
    spreadsheet_sheet_filter: SpreadsheetSheetFilter
    spreadsheet_sheet_filter_view: SpreadsheetSheetFilterView
    spreadsheet_sheet_filter_view_condition: SpreadsheetSheetFilterViewCondition
    spreadsheet_sheet_float_image: SpreadsheetSheetFloatImage
    def __init__(self, config: Config) -> None: ...
