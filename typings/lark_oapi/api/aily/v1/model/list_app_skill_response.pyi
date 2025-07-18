from .list_app_skill_response_body import ListAppSkillResponseBody as ListAppSkillResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAppSkillResponse(BaseResponse):
    data: ListAppSkillResponseBody | None
    def __init__(self, d=None) -> None: ...
