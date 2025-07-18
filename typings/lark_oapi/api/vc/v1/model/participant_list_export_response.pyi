from .participant_list_export_response_body import ParticipantListExportResponseBody as ParticipantListExportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ParticipantListExportResponse(BaseResponse):
    data: ParticipantListExportResponseBody | None
    def __init__(self, d=None) -> None: ...
