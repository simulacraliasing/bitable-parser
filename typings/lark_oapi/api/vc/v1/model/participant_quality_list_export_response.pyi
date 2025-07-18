from .participant_quality_list_export_response_body import ParticipantQualityListExportResponseBody as ParticipantQualityListExportResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ParticipantQualityListExportResponse(BaseResponse):
    data: ParticipantQualityListExportResponseBody | None
    def __init__(self, d=None) -> None: ...
