from ..model.download_file_request import DownloadFileRequest as DownloadFileRequest
from ..model.download_file_response import DownloadFileResponse as DownloadFileResponse
from ..model.upload_file_request import UploadFileRequest as UploadFileRequest
from ..model.upload_file_response import UploadFileResponse as UploadFileResponse
from lark_oapi.core import JSON as JSON
from lark_oapi.core.const import APPLICATION_JSON as APPLICATION_JSON, CONTENT_TYPE as CONTENT_TYPE, UTF_8 as UTF_8
from lark_oapi.core.http import Transport as Transport
from lark_oapi.core.model import Config as Config, RawResponse as RawResponse, RequestOption as RequestOption
from lark_oapi.core.token import verify as verify
from lark_oapi.core.utils import Files as Files

class File:
    config: Config
    def __init__(self, config: Config) -> None: ...
    def download(self, request: DownloadFileRequest, option: RequestOption | None = None) -> DownloadFileResponse: ...
    async def adownload(self, request: DownloadFileRequest, option: RequestOption | None = None) -> DownloadFileResponse: ...
    def upload(self, request: UploadFileRequest, option: RequestOption | None = None) -> UploadFileResponse: ...
    async def aupload(self, request: UploadFileRequest, option: RequestOption | None = None) -> UploadFileResponse: ...
