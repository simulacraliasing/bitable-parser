from .get_app_skill_response_body import GetAppSkillResponseBody as GetAppSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class GetAppSkillResponse(BaseResponse):
    data: GetAppSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
