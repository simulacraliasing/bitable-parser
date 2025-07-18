from ..model.create_file_request import CreateFileRequest as CreateFileRequest
from ..model.create_file_response import CreateFileResponse as CreateFileResponse
from ..model.get_file_request import GetFileRequest as GetFileRequest
from ..model.get_file_response import GetFileResponse as GetFileResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class File:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def create(self, request: CreateFileRequest, option: RequestOption | None = None) -> CreateFileResponse: ...
    async def acreate(self, request: CreateFileRequest, option: RequestOption | None = None) -> CreateFileResponse: ...
    def get(self, request: GetFileRequest, option: RequestOption | None = None) -> GetFileResponse: ...
    async def aget(self, request: GetFileRequest, option: RequestOption | None = None) -> GetFileResponse: ...
