from .batch_get_tmp_download_url_media_response_body import BatchGetTmpDownloadUrlMediaResponseBody as BatchGetTmpDownloadUrlMediaResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchGetTmpDownloadUrlMediaResponse(BaseResponse):
    data: BatchGetTmpDownloadUrlMediaResponseBody | None
    def __init__(self, d=None) -> None: ...
