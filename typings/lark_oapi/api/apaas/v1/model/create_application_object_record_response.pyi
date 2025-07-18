from .create_application_object_record_response_body import CreateApplicationObjectRecordResponseBody as CreateApplicationObjectRecordResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class CreateApplicationObjectRecordResponse(BaseResponse):
    data: CreateApplicationObjectRecordResponseBody | None
    def __init__(self, d=None) -> None: ...
