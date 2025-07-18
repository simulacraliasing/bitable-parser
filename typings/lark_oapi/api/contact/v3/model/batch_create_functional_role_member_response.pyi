from .batch_create_functional_role_member_response_body import BatchCreateFunctionalRoleMemberResponseBody as BatchCreateFunctionalRoleMemberResponseBody
from lark_oapi.core.construct import init as init
from lark_oapi.core.model import BaseResponse as BaseResponse

class BatchCreateFunctionalRoleMemberResponse(BaseResponse):
    data: BatchCreateFunctionalRoleMemberResponseBody | None
    def __init__(self, d=None) -> None: ...
