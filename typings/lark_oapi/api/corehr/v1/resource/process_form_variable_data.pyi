from ..model.get_process_form_variable_data_request import GetProcessFormVariableDataRequest as GetProcessFormVariableDataRequest
from ..model.get_process_form_variable_data_response import GetProcessFormVariableDataResponse as GetProcessFormVariableDataResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files
from requests_toolbelt import MultipartEncoder as MultipartEncoder

class ProcessFormVariableData:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def get(self, request: GetProcessFormVariableDataRequest, option: RequestOption | None = None) -> GetProcessFormVariableDataResponse: ...
    async def aget(self, request: GetProcessFormVariableDataRequest, option: RequestOption | None = None) -> GetProcessFormVariableDataResponse: ...
