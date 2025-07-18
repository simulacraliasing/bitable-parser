from .meeting_list_export_response_body import MeetingListExportResponseBody as MeetingListExportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class MeetingListExportResponse(BaseResponse):
    data: MeetingListExportResponseBody | None
    def __init__(self, d=None) -> None: ...
