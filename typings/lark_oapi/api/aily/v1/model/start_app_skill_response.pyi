from .start_app_skill_response_body import StartAppSkillResponseBody as StartAppSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class StartAppSkillResponse(BaseResponse):
    data: StartAppSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
