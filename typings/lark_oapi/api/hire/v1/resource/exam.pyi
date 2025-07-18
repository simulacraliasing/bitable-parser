from ..model.create_exam_request import CreateExamRequest as CreateExamRequest
from ..model.create_exam_response import CreateExamResponse as CreateExamResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Exam:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateExamRequest, option: RequestOption | None = None) -> CreateExamResponse: ...
    async def acreate(self, request: CreateExamRequest, option: RequestOption | None = None) -> CreateExamResponse: ...
