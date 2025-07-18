from .get_participant_quality_list_response_body import GetParticipantQualityListResponseBody as GetParticipantQualityListResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetParticipantQualityListResponse(BaseResponse):
    data: GetParticipantQualityListResponseBody | None
    def __init__(self, d=None) -> None: ...
