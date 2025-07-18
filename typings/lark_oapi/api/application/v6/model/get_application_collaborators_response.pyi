from .get_application_collaborators_response_body import GetApplicationCollaboratorsResponseBody as GetApplicationCollaboratorsResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetApplicationCollaboratorsResponse(BaseResponse):
    data: GetApplicationCollaboratorsResponseBody | None
    def __init__(self, d=None) -> None: ...
