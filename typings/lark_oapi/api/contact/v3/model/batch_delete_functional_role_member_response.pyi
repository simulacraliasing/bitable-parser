from .batch_delete_functional_role_member_response_body import BatchDeleteFunctionalRoleMemberResponseBody as BatchDeleteFunctionalRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchDeleteFunctionalRoleMemberResponse(BaseResponse):
    data: BatchDeleteFunctionalRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
