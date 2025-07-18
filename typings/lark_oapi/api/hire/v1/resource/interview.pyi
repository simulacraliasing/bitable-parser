from ..model.get_by_talent_interview_request import GetByTalentInterviewRequest as GetByTalentInterviewRequest
from ..model.get_by_talent_interview_response import GetByTalentInterviewResponse as GetByTalentInterviewResponse
from ..model.list_interview_request import ListInterviewRequest as ListInterviewRequest
from ..model.list_interview_response import ListInterviewResponse as ListInterviewResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class Interview:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get_by_talent(self, request: GetByTalentInterviewRequest, option: RequestOption | None = None) -> GetByTalentInterviewResponse: ...
    async def aget_by_talent(self, request: GetByTalentInterviewRequest, option: RequestOption | None = None) -> GetByTalentInterviewResponse: ...
    def list(self, request: ListInterviewRequest, option: RequestOption | None = None) -> ListInterviewResponse: ...
    async def alist(self, request: ListInterviewRequest, option: RequestOption | None = None) -> ListInterviewResponse: ...
