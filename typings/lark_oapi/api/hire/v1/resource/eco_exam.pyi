from ..model.login_info_eco_exam_request import LoginInfoEcoExamRequest as LoginInfoEcoExamRequest
from ..model.login_info_eco_exam_response import LoginInfoEcoExamResponse as LoginInfoEcoExamResponse
from ..model.update_result_eco_exam_request import UpdateResultEcoExamRequest as UpdateResultEcoExamRequest
from ..model.update_result_eco_exam_response import UpdateResultEcoExamResponse as UpdateResultEcoExamResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class EcoExam:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def login_info(self, request: LoginInfoEcoExamRequest, option: RequestOption | None = None) -> LoginInfoEcoExamResponse: ...
    async def alogin_info(self, request: LoginInfoEcoExamRequest, option: RequestOption | None = None) -> LoginInfoEcoExamResponse: ...
    def update_result(self, request: UpdateResultEcoExamRequest, option: RequestOption | None = None) -> UpdateResultEcoExamResponse: ...
    async def aupdate_result(self, request: UpdateResultEcoExamRequest, option: RequestOption | None = None) -> UpdateResultEcoExamResponse: ...
