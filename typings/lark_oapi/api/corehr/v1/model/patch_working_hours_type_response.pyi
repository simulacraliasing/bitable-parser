from .patch_working_hours_type_response_body import PatchWorkingHoursTypeResponseBody as PatchWorkingHoursTypeResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class PatchWorkingHoursTypeResponse(BaseResponse):
    data: PatchWorkingHoursTypeResponseBody | None
    def __init__(self, d=None) -> None: ...
