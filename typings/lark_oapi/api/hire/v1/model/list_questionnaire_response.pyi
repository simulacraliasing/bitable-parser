from .list_questionnaire_response_body import ListQuestionnaireResponseBody as ListQuestionnaireResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListQuestionnaireResponse(BaseResponse):
    data: ListQuestionnaireResponseBody | None
    def __init__(self, d=None) -> None: ...
