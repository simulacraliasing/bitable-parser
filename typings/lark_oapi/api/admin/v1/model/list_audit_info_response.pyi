from .list_audit_info_response_body import ListAuditInfoResponseBody as ListAuditInfoResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class ListAuditInfoResponse(BaseResponse):
    data: ListAuditInfoResponseBody | None
    def __init__(self, d=None) -> None: ...
