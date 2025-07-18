from .patch_task_response_body import PatchTaskResponseBody as PatchTaskResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchTaskResponse(BaseResponse):
    data: PatchTaskResponseBody | None
    def __init__(self, d=None) -> None: ...
