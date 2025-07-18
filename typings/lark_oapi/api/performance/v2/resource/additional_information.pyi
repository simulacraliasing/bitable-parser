from ..model.import_additional_information_request import ImportAdditionalInformationRequest as ImportAdditionalInformationRequest
from ..model.import_additional_information_response import ImportAdditionalInformationResponse as ImportAdditionalInformationResponse
from ..model.query_additional_information_request import QueryAdditionalInformationRequest as QueryAdditionalInformationRequest
from ..model.query_additional_information_response import QueryAdditionalInformationResponse as QueryAdditionalInformationResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class AdditionalInformation:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def import_(self, request: ImportAdditionalInformationRequest, option: RequestOption | None = None) -> ImportAdditionalInformationResponse: ...
    async def aimport_(self, request: ImportAdditionalInformationRequest, option: RequestOption | None = None) -> ImportAdditionalInformationResponse: ...
    def query(self, request: QueryAdditionalInformationRequest, option: RequestOption | None = None) -> QueryAdditionalInformationResponse: ...
    async def aquery(self, request: QueryAdditionalInformationRequest, option: RequestOption | None = None) -> QueryAdditionalInformationResponse: ...
