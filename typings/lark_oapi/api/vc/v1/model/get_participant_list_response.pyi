from .get_participant_list_response_body import GetParticipantListResponseBody as GetParticipantListResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetParticipantListResponse(BaseResponse):
    data: GetParticipantListResponseBody | None
    def __init__(self, d=None) -> None: ...
